# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_contactusmsg'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('term', models.TextField()),
                ('num_results', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('searcher', models.ForeignKey(to='jobapp.Userinfo')),
            ],
        ),
    ]
