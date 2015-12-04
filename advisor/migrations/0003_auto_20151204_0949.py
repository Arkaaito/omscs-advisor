# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import advisor.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_offering_instructors'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='offered_from',
            field=advisor.models.TermField(default='Spring2014'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offering',
            name='course',
            field=models.ForeignKey(related_query_name=b'offering', related_name='offerings', to='advisor.Course'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='user',
            field=models.ForeignKey(related_query_name=b'plan', related_name='plans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='user',
            field=models.OneToOneField(related_query_name=b'preferences', related_name='preferences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='privacy',
            name='user',
            field=models.OneToOneField(related_query_name=b'privacy', related_name='privacy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_query_name=b'profile', related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(related_query_name=b'review', related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
