# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_searchterm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchterm',
            name='searcher',
            field=models.ForeignKey(to='jobapp.Userinfo', null=True),
        ),
    ]
