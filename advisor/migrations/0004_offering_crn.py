# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0003_auto_20151204_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='crn',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
