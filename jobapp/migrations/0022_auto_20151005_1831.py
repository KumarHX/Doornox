# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0021_auto_20151003_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='lnkd_img_url',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 18, 31, 19, 816445)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 18, 31, 19, 817697)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 18, 31, 19, 815273)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 18, 31, 19, 815242)),
        ),
    ]
