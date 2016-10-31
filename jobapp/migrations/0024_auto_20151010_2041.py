# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0023_auto_20151010_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='additional_comments',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 41, 49, 617227)),
        ),
        migrations.AlterField(
            model_name='job',
            name='glassdoor_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 41, 49, 618167)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='company',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 41, 49, 616067)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='fbid',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='funny_saying',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gid',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='goog_img_url',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='job_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 20, 41, 49, 616033)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lnkd_img_url',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lnkd_pubprofile',
            field=models.TextField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='lnkdid',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='resume_link',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='work_location',
            field=models.TextField(blank=True),
        ),
    ]
