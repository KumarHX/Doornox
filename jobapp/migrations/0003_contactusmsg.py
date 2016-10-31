# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_job_additional_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]
