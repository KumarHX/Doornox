# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_auto_20150905_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='career_level',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 9, 1, 13, 44, 440736)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 9, 1, 13, 44, 441577)),
        ),
    ]
