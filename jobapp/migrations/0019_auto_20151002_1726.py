# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0018_auto_20150924_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 17, 26, 15, 29190)),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='num_logins',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 17, 26, 15, 30260)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 17, 26, 15, 31683)),
        ),
    ]
