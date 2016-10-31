# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.TextField()),
                ('location', models.TextField()),
                ('job_title', models.TextField()),
                ('job_description', models.TextField()),
                ('salary_min', models.IntegerField(default=10000)),
                ('salary_max', models.IntegerField(default=1000000)),
                ('career_level', models.IntegerField(default=0)),
                ('company_link', models.TextField()),
                ('glassdoor_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to_email', models.TextField()),
                ('message', models.TextField()),
                ('content', models.TextField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver_email', models.TextField()),
                ('preference', models.IntegerField()),
                ('cover_letter_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Starred',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.ForeignKey(to='jobapp.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.TextField()),
                ('lname', models.TextField()),
                ('email', models.TextField()),
                ('fbid', models.CharField(max_length=20)),
                ('lnkdid', models.CharField(max_length=20)),
                ('gid', models.CharField(max_length=20)),
                ('location', models.TextField()),
                ('work_location', models.TextField()),
                ('company', models.TextField()),
                ('job_title', models.TextField()),
                ('funny_saying', models.TextField()),
                ('resume_link', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='starred',
            name='user',
            field=models.ForeignKey(to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='receiver',
            field=models.ForeignKey(to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='recommendee',
            field=models.ForeignKey(related_name='recommendee_user', to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='recommender',
            field=models.ForeignKey(related_name='recommender_user', to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='message',
            name='_from',
            field=models.ForeignKey(related_name='from_user', to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='message',
            name='_to',
            field=models.ForeignKey(related_name='to_user', to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='job',
            name='poster',
            field=models.ForeignKey(to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_1',
            field=models.ForeignKey(related_name='user_1_user', to='jobapp.Userinfo'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_2',
            field=models.ForeignKey(related_name='user_2_user', to='jobapp.Userinfo'),
        ),
    ]
