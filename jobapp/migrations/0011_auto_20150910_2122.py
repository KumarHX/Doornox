# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_auto_20150910_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 21, 22, 2, 292733)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 21, 22, 2, 293596)),
        ),
    ]
