# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_job_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 4, 12, 11, 604813)),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 4, 12, 11, 603155)),
        ),
    ]
