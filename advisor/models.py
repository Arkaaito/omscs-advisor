from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Term(models.CharField(max_length=10)):
    FIRST = 'Spring2014'

class Profile(models.Model):
    PROSPECT = 'P'
    NEW_ADMIT = 'N'
    CURRENT_STUDENT = 'C'
    EX_STUDENT = 'E'
    MATURE_STUDENT = 'M'
    GRADUATE = 'G'
    FROG = 'F'
    OTHER = 'O'
    VALID_STATUSES = (
        (PROSPECT, 'Prospective Student'),
        (NEW_ADMIT, 'New Student'),
        (CURRENT_STUDENT, 'Current Student'),
        (EX_STUDENT, 'On Sabbatical'),
        (MATURE_STUDENT, 'Student Emeritus'),
        (GRADUATE, 'Alumnus'),
        (FROG, 'Froggy Friend'),
        (OTHER, 'Faculty/Staff'),
    )

    user = models.OneToOneField(User)
    friends = models.ForeignKey(User)
    status = models.CharField(max_length=1, choices=VALID_STATUSES, default=CURRENT_STUDENT)
    bio = models.TextField(blank=True)
    # timezone = models.TimeField()
    location = models.CharField(max_length=50, blank=True)
    start_date = Term(default=Term.FIRST)
    linkedin_id = models.CharField(max_length=50, blank=True)
    facebook_id = models.CharField(max_length=50, blank=True)
    google_id = models.CharField(max_length=50, blank=True)

class Preferences(models.Model):
    user = models.OneToOneField(User)
    specializations = models.ManyToManyField(Specialization)
    # primary_specializations = models.ManyToManyField(Specialization)
    # secondary_specializations = models.ManyToManyField(Specialization)
    allow_proctortrack = models.BooleanField(default=True)
    allow_groupwork = models.BooleanField(default=True)
    max_hours = models.PositiveSmallIntegerField(default=20)

class Plan(models.Model):
    user = models.OneToOneField(User)
    offerings = models.ManyToManyField(Offering)
    target_term = Term()

class Privacy(models.Model):
    PRIVATE = 0
    FRIENDS = 1
    REGISTERED = 2
    WORLD = 3
    PRIVACY_CHOICES = (
        (PRIVATE, 'Private'),
        (FRIENDS, 'Friends'),
        (REGISTERED, 'Registered Users'),
        (WORLD, 'Everyone'),
    )

    user = models.OneToOneField(User)
    share_overall = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_specializations = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_bio = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_contact = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_timezone = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_location = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_reviews = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)
    share_plan = models.PositiveSmallIntegerField(choices=PRIVACY_CHOICES, default=FRIENDS)

class Course(models.Model):
    key = models.CharField(max_length=10) # like "AIR"
    number = models.CharField(max_length=10) # like "CS8803-O01"
    offered_from = Term() # like "Summer2014"
    offered_summers = models.BooleanField(default=False) # true or false
    title = models.CharField(max_length=100) # like "Special Topics: Artificial Intelligence for Robotics"
    summary = models.TextField() # like "Learn how to program all the major systems of a robotic car..."
    info_link = models.URLField(max_length=200, null=True) # like "http://www.omscs.gatech.edu/cs-8803-artificial-intelligence-robotics/"
    syllabus_link = models.URLField(max_length=200, null=True)
    readiness_link = models.URLField(max_length=200, null=True)
    primary_specialization = models.ForeignKey(Specialization, null=True)

class Offering(models.Model):
    course = models.ForeignKey(Course)
    term = Term()
    grades_udacity = models.BooleanField()
    grades_piazza = models.BooleanField()
    proctored_exams = models.PositiveSmallIntegerField()
    timed_exams = models.PositiveSmallIntegerField()
    open_book_exams = models.PositiveSmallIntegerField()
    group_assignments = models.PositiveSmallIntegerField()
    coding_assignments = models.PositiveSmallIntegerField()
    written_assignments = models.PositiveSmallIntegerField()

    average_difficulty = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    average_value = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    median_peak_effort = models.DecimalField(max_digits=5, decimal_places=3, default=15)
    median_typical_effort = models.DecimalField(max_digits=5, decimal_places=3, default=10)
    time_to_fill = models.PositiveIntegerField(default=1440) # how many minutes after the start of registration did the offering fill?

class Review(models.Model):
    GRADE_A = 4.0
    GRADE_B = 3.0
    GRADE_C = 2.0
    GRADE_D = 1.0
    GRADE_F = 0.0
    VALID_GRADES = (
        (GRADE_A, 'A'),
        (GRADE_B, 'B'),
        (GRADE_C, 'C'),
        (GRADE_D, 'D'),
        (GRADE_F, 'F'),
    )
    # TODO: similar choices for the star ratings, or are we using a custom form control?

    user = models.ForeignKey(User)
    offering = models.ForeignKey(Offering)
    withdrawn = models.BooleanField()
    grade = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True, choices=VALID_GRADES)
    difficulty_rating = models.DecimalField(max_digits=1, decimal_places=0, null=True)
    value_rating = models.DecimalField(max_digits=1, decimal_places=0, null=True)
    peak_effort = models.PositiveSmallIntegerField(null=True)
    typical_effort = models.PositiveSmallIntegerField(null=True)
    comments = models.TextField(blank=True)
    anonymous = models.BooleanField(default=False)

class Specialization(models.Model):
    key = models.CharField(max_length=10) # like "ML"
    name = models.CharField(max_length=50) # like "Machine Learning"
    requirements = models.ForeignKey(Requirement) # link to the top-level requirement

class Requirement(models.Model):
    ONE_OF = 'oneOf'
    TWO_OF = 'twoOf'
    THREE_OF = 'threeOf'
    ALL_OF = 'allOf'
    CONSTRAINT_TYPES = (
        (ONE_OF, ONE_OF),
        (TWO_OF, TWO_OF),
        (THREE_OF, THREE_OF),
        (ALL_OF, ALL_OF),
    )

    specialization = models.ForeignKey(Specialization)
    parent = models.ForeignKey('self', null=True)
    course = models.ForeignKey(Course, null=True)
    type = models.CharField(maxLength=8, choices=CONSTRAINT_TYPES)

class Announcement(models.Model):
    title = models.TextField()
    body = models.TextField()
    posted = models.DateTimeField()

class Notification(models.Model):
    announcement = models.ForeignKey(Announcement, null=True)
    title = models.TextField()
    body = models.TextField()
    triggered = models.DateTimeField()