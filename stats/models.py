from django.db import models
from advisor.models import *


class EnrollmentSnapshot(models.Model):
    offering = models.ForeignKey(Offering, related_name='snapshots', related_query_name='snapshot')

    recorded = models.DateTimeField()

    real_cap = models.PositiveIntegerField()
    real_full = models.PositiveIntegerField()
    real_open = models.PositiveIntegerField()

    waitlist_cap = models.PositiveIntegerField()
    waitlist_full = models.PositiveIntegerField()
    waitlist_open = models.PositiveIntegerField()

    def __str__(self):
        return self.offering.course.number + ": " + self.offering.term + " @" + str(self.recorded) + " ("\
               + ",".join([self.real_cap, self.real_full, self.real_open, self.waitlist_cap, self.waitlist_full, self.waitlist_open])\
               + ")"
