# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_auto_20150831_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 23, 47, 53, 50541)),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_max',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_min',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 5, 23, 47, 53, 51916)),
        ),
    ]
