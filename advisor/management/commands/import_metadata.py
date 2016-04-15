from django.core.exceptions import ObjectDoesNotExist

__author__ = 'arkaaito'

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omscs.settings")

import json
from django.core.management.base import BaseCommand
from advisor.config import Term
from advisor.models import Course
from advisor.models import Offering
from advisor.models import Specialization
from advisor.models import Requirement

class Command(BaseCommand):
    args = '/path/to/course-metadata.js /path/to/specialization-metadata.js'
    help = 'Import new course/specialization metadata or update the old stuff.'

    def add_arguments(self, parser):
        parser.add_argument('course-data', nargs=1)
        parser.add_argument('specialization-data', nargs=1)

    def build_requirements(self, specialization, type, value):
        req = Requirement()
        req.linked_specialization = specialization
        req.type = type
        if isinstance(value, dict):
            if (len(value.keys()) == 1) & (type == Requirement.ALL_OF):
                # Collapse by one level.
                req = self.build_requirements(specialization, value.keys()[0], value[value.keys()[0]])
                req.save()
            else:
                req.save()
                for key in value.keys():
                    child = self.build_requirements(specialization, key, value[key])
                    child.parent = req
                    child.save()
        elif isinstance(value, list):
            if (len(value) == 1) & (type == Requirement.ALL_OF):
                # Collapse by one level.
                req = self.build_requirements(specialization, Requirement.ALL_OF, value[0])
                req.save()
            else:
                req.save()
                for val in list:
                    child = self.build_requirements(specialization, Requirement.ALL_OF, val)
                    child.parent = req
                    child.save()
        else:
            req.course = value
            req.save()
        return req

    def handle(self, *args, **options):
        specialization_file = open(options['specialization-data'][0])
        raw_specializations = json.load(specialization_file)
        for raw_specialization in raw_specializations:
            # Create a specialization entry
            try:
                s = Specialization.objects.get(key=raw_specialization["specializationId"])
            except ObjectDoesNotExist:
                s = Specialization()
                s.key = raw_specialization["specializationId"]
            s.name = raw_specialization["specializationName"]
            s.save()
            # s.requirements = self.build_requirements(s, Requirement.ALL_OF, raw_specialization[Requirement.ALL_OF])
            # TODO: Current method leads to "orphaned" requirements.  Fix this?
        specialization_file.close()

        course_file = open(options['course-data'][0])
        raw_courses = json.load(course_file)
        for raw_course in raw_courses:
            # For each course, create or update Course
            # TODO: many issues will arise if metadata is not already sorted by date.
            try:
                c = Course.objects.get(key=raw_course["Id"])
            except ObjectDoesNotExist:
                c = Course()
                c.key = raw_course["Id"]
            start_term = raw_course["EffectiveFrom"]
            c.offered_from = Term.min(c.offered_from, start_term)
            c.offered_summers = c.offered_summers | raw_course["Summer"]
            if "Number" in raw_course:
                c.number = raw_course["Number"]

            if "Title" in raw_course:
                c.title = raw_course["Title"]
            if "Summary" in raw_course:
                c.summary = raw_course["Summary"]
            if "Syllabus" in raw_course:
                c.syllabus_link = raw_course["Syllabus"]
            if "Readiness" in raw_course:
                c.readiness_link = raw_course["Readiness"]
            if "Specialization" in raw_course:
                c.primary_specialization = Specialization.objects.get(key=raw_course["Specialization"])
            c.save()
            # Now create or update each Offering on or after the date given
            terms = Term.range(start_term, Term.HORIZON, summer=raw_course["Summer"])
            for term in terms:
                try:
                    o = Offering.objects.get(course=c, term=term)
                except ObjectDoesNotExist:
                    o = Offering()
                    o.course = c
                    o.term = term
                    o.grades_udacity = False
                    o.grades_piazza = False
                    o.proctored_exams = 0
                    o.timed_exams = 0
                    o.open_book_exams = 0
                    o.group_assignments = 0
                    o.coding_assignments = 0
                    o.written_assignments = 0
                    o.instructors = "Unknown"
                if "Instructors" in raw_course:
                    o.instructors = "; ".join(raw_course["Instructors"])
                if "UdacityRequired" in raw_course:
                    o.grades_udacity = raw_course["UdacityRequired"]
                if "PiazzaRequired" in raw_course:
                    o.grades_piazza = raw_course["PiazzaRequired"]
                if "ProctoredExams" in raw_course:
                    o.proctored_exams = raw_course["ProctoredExams"]
                if "TimedExams" in raw_course:
                    o.timed_exams = raw_course["TimedExams"]
                if "OpenBookExams" in raw_course:
                    o.open_book_exams = raw_course["OpenBookExams"]
                if "GroupAssignments" in raw_course:
                    o.group_assignments = raw_course["GroupAssignments"]
                if "CodingAssignments" in raw_course:
                    o.coding_assignments = raw_course["CodingAssignments"]
                if "WrittenAssignments" in raw_course:
                    o.written_assignments = raw_course["WrittenAssignments"]
                o.save()
        course_file.close()