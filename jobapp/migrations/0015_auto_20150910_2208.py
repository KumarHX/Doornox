# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0014_auto_20150910_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='lnkd_pubprofile',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 22, 8, 49, 935209)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 22, 8, 49, 936158)),
        ),
    ]
