# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0017_auto_20150912_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='goog_img_url',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 18, 7, 36, 645870)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 18, 7, 36, 647681)),
        ),
    ]
