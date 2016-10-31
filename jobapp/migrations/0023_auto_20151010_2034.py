# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0022_auto_20151005_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 34, 14, 920649)),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 34, 14, 923154)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 34, 14, 919450)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 34, 14, 919415)),
        ),
    ]
