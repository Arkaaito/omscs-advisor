import os
import re

from time import strptime, mktime
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from bs4 import BeautifulSoup

from advisor.models import Offering
from stats.models import EnrollmentSnapshot


class Command(BaseCommand):
    help = 'Import the specified OSCAR crawl file into a set of enrollment_snapshots'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+')

    def real_cap_up_trigger(self, course, old, new):
        print("Cap increase notice", "Cap increased for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])
        #send_mail("Cap increase notice", "Cap increased for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])

    def waitlist_cap_up_trigger(self, course, old, new):
        print("Cap increase notice", "Waitlist size increased for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])
        #send_mail("Cap increase notice", "Waitlist size increased for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])

    def waitlist_open_trigger(self, course, size):
        print("Waitlist notice", "Waitlist opened for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])
        #send_mail("Waitlist notice", "Waitlist opened for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])

    def real_open_seat_trigger(self, course, old, new):
        print("Open seat", "Someone canceled their registration for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])
        #send_mail("Open seat", "Someone canceled their registration for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])

    def waitlist_open_seat_trigger(self, course, old, new):
        print("Open seat", "Someone left the waitlist for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])
        #send_mail("Open seat", "Someone left the waitlist for "+course.course.number, 'oscar-monitor@omscs.net', ['alstisgi@gmail.com'])

    def handle(self, *args, **options):
        #process_filename = "/var/crawl-processing"
        process_filename = "/Users/Arkaaito/Documents/Classes/GATech/CS6460/crawl-processing"
        for filename in options['filename']:
            try:
                # Rotate crawlfile to new location so the crawler doesn't append while we're working
                os.rename(filename, process_filename)
                with open(process_filename, 'r') as crawlfile:
                    while crawlfile.readline():
                        parts = []
                        # Split apart on Started at\nDate, Finished at\nDate
                        line = crawlfile.readline() # Eat the opening date line
                        line = crawlfile.readline() # ... and the first curl line
                        part = []
                        while (line is not None) & (line != "") & (line.strip() != "Finished at"):
                            if '--_curl_--' in line:
                                if len(part) > 0:
                                    parts.append(part)
                                    part = []
                            else:
                                part.append(line)
                            line = crawlfile.readline()

                        date_string = crawlfile.readline().strip()
                        if date_string.strip() == "":
                            continue
                        crawled_time = datetime.fromtimestamp(mktime(strptime(date_string, "%a %b  %d %H:%M:%S %Z %Y")))
                        for part in parts:
                            # Load with the HTML parser
                            tree = BeautifulSoup("".join(part), "html.parser")
                            tables = tree.find_all('table', attrs={"class":"datadisplaytable"})
                            # Find elements corresponding to course name, course number, associated term
                            info_table = tables[0]
                            info = re.split(r' - ', info_table.find('th').contents[0])
                            title = info[0]
                            number = "".join(info[2].split(' '))
                            if number == 'CS8803':
                                mappings = {
                                    'O01': 'AIR',
                                    'O02': 'IOS',
                                    'O03': 'RL',
                                    'O04': 'ES',
                                    'O05': 'DV',
                                    'O06': 'BA'
                                }
                                number = number + '-' + mappings[info[3]]
                            term = "".join(info_table.find('td').contents[2].strip().split())
                            if "Long Title" in str(info_table.find('td').contents[1]):
                                term = "".join(info_table.find('td').contents[6].strip().split())
                            # Look up course by number
                            # Validating with name or instructor doesn't quite work because the OSCAR info can have errors
                            print "Loading for course "+number+" in "+term
                            offering = Offering.objects.get(course__number=number, term=term)
                            last_obs = None
                            try:
                                last_obs = EnrollmentSnapshot.objects.filter(offering=offering).latest('recorded')
                            except:
                                last_obs = None # Ignore this; we won't set off any triggers in this case.
                            # Find elements corresponding to {seats, waitlist seats} x {capacity, actual, remaining}
                            seats_data = map(lambda x: int(x.contents[0]), tables[1].find_all('td', attrs={"class":"dddefault"}))
                            real_cap = seats_data[0]
                            real_full = seats_data[1]
                            real_open = seats_data[2]
                            waitlist_cap = seats_data[3]
                            waitlist_full = seats_data[4]
                            waitlist_open = seats_data[5]
                            # Save snapshot into DB
                            obs = EnrollmentSnapshot()
                            obs.offering = offering
                            obs.recorded = crawled_time
                            obs.real_cap = real_cap
                            obs.real_full = real_full
                            obs.real_open = real_open
                            obs.waitlist_cap = waitlist_cap
                            obs.waitlist_full = waitlist_full
                            obs.waitlist_open = waitlist_open
                            obs.save()

                            # Compare with last enrollment_snapshot for this course, and trigger relevant events
                            if last_obs is None: last_obs = obs

                            # For course seats:
                            if obs.real_cap > last_obs.real_cap:
                                self.real_cap_up_trigger(offering, last_obs.real_cap, obs.real_cap)
                            elif obs.real_open > last_obs.real_open:
                                self.real_open_seat_trigger(offering, last_obs.real_open, obs.real_open)

                            # And waitlist spots
                            if (obs.waitlist_cap > 0) & (last_obs.waitlist_cap == 0):
                                self.waitlist_open_trigger(offering, obs.waitlist_cap)
                            elif obs.waitlist_cap > last_obs.waitlist_cap:
                                self.waitlist_cap_up_trigger(offering, last_obs.waitlist_cap, obs.waitlist_cap)
                            elif obs.waitlist_open > last_obs.waitlist_open:
                                self.waitlist_open_seat_trigger(offering, last_obs.waitlist_open, last_obs.waitlist_open)
                crawlfile.close()
                os.remove(process_filename)
            except IOError as e:
                print "failed to open "+filename+": ({0}) / {1}\n, ignoring".format(e.errno, e.strerror)