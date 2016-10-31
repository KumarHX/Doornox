# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_auto_20150911_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='attachment_path',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 18, 41, 19, 486629)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 12, 18, 41, 19, 488304)),
        ),
    ]
