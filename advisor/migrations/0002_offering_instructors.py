# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='instructors',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
