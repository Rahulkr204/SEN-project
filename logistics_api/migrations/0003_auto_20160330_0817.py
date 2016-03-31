# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0002_auto_20160329_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='waypoint',
            field=models.CharField(max_length=360),
        ),
    ]
