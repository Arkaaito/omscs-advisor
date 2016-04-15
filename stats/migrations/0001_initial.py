# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0003_auto_20151204_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentSnapshot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recorded', models.DateTimeField()),
                ('real_cap', models.PositiveIntegerField()),
                ('real_full', models.PositiveIntegerField()),
                ('real_open', models.PositiveIntegerField()),
                ('waitlist_cap', models.PositiveIntegerField()),
                ('waitlist_full', models.PositiveIntegerField()),
                ('waitlist_open', models.PositiveIntegerField()),
                ('offering', models.ForeignKey(related_query_name=b'snapshot', related_name='snapshots', to='advisor.Offering')),
            ],
        ),
    ]
