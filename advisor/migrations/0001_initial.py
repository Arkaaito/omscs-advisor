# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import advisor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('posted', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('offered_summers', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('info_link', models.URLField(null=True)),
                ('syllabus_link', models.URLField(null=True)),
                ('readiness_link', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('triggered', models.DateTimeField()),
                ('announcement', models.ForeignKey(to='advisor.Announcement', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', advisor.models.TermField()),
                ('grades_udacity', models.BooleanField()),
                ('grades_piazza', models.BooleanField()),
                ('proctored_exams', models.PositiveSmallIntegerField()),
                ('timed_exams', models.PositiveSmallIntegerField()),
                ('open_book_exams', models.PositiveSmallIntegerField()),
                ('group_assignments', models.PositiveSmallIntegerField()),
                ('coding_assignments', models.PositiveSmallIntegerField()),
                ('written_assignments', models.PositiveSmallIntegerField()),
                ('average_difficulty', models.DecimalField(default=0, max_digits=4, decimal_places=3)),
                ('average_value', models.DecimalField(default=0, max_digits=4, decimal_places=3)),
                ('median_peak_effort', models.DecimalField(default=15, max_digits=5, decimal_places=3)),
                ('median_typical_effort', models.DecimalField(default=10, max_digits=5, decimal_places=3)),
                ('time_to_fill', models.PositiveIntegerField(default=1440)),
                ('course', models.ForeignKey(to='advisor.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_term', advisor.models.TermField()),
                ('offerings', models.ManyToManyField(to='advisor.Offering')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('allow_proctortrack', models.BooleanField(default=True)),
                ('allow_groupwork', models.BooleanField(default=True)),
                ('max_hours', models.PositiveSmallIntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_overall', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_specializations', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_bio', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_contact', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_timezone', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_location', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_reviews', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('share_plan', models.PositiveSmallIntegerField(default=1, choices=[(0, b'Private'), (1, b'Friends'), (2, b'Registered Users'), (3, b'Everyone')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'C', max_length=1, choices=[(b'P', b'Prospective Student'), (b'N', b'New Student'), (b'C', b'Current Student'), (b'E', b'On Sabbatical'), (b'M', b'Student Emeritus'), (b'G', b'Alumnus'), (b'F', b'Froggy Friend'), (b'O', b'Faculty/Staff')])),
                ('bio', models.TextField(blank=True)),
                ('location', models.CharField(max_length=50, blank=True)),
                ('start_date', advisor.models.TermField(default=b'Spring2014')),
                ('linkedin_id', models.CharField(max_length=50, blank=True)),
                ('facebook_id', models.CharField(max_length=50, blank=True)),
                ('google_id', models.CharField(max_length=50, blank=True)),
                ('friends', models.ManyToManyField(related_query_name=b'follower', related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=8, choices=[(b'oneOf', b'oneOf'), (b'twoOf', b'twoOf'), (b'threeOf', b'threeOf'), (b'allOf', b'allOf')])),
                ('course', models.ForeignKey(to='advisor.Course', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('withdrawn', models.BooleanField()),
                ('grade', models.DecimalField(blank=True, null=True, max_digits=1, decimal_places=0, choices=[(4.0, b'A'), (3.0, b'B'), (2.0, b'C'), (1.0, b'D'), (0.0, b'F')])),
                ('difficulty_rating', models.DecimalField(null=True, max_digits=1, decimal_places=0)),
                ('value_rating', models.DecimalField(null=True, max_digits=1, decimal_places=0)),
                ('peak_effort', models.PositiveSmallIntegerField(null=True)),
                ('typical_effort', models.PositiveSmallIntegerField(null=True)),
                ('comments', models.TextField(blank=True)),
                ('anonymous', models.BooleanField(default=False)),
                ('offering', models.ForeignKey(to='advisor.Offering')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('requirements', models.ForeignKey(to='advisor.Requirement', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='requirement',
            name='linked_specialization',
            field=models.ForeignKey(to='advisor.Specialization'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='parent',
            field=models.ForeignKey(to='advisor.Requirement', null=True),
        ),
        migrations.AddField(
            model_name='preferences',
            name='specializations',
            field=models.ManyToManyField(to='advisor.Specialization'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='primary_specialization',
            field=models.ForeignKey(to='advisor.Specialization', null=True),
        ),
    ]
