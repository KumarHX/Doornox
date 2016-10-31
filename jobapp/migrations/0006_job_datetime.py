# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_auto_20150829_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 31, 3, 39, 50, 165593)),
        ),
    ]
