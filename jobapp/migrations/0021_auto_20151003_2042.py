# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0020_auto_20151002_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 42, 21, 594410)),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 42, 21, 601132)),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 42, 21, 602606)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 3, 20, 42, 21, 594510)),
        ),
    ]
