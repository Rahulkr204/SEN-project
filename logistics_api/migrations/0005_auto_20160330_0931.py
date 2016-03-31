# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0004_auto_20160330_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='waypoint',
            field=models.CharField(max_length=60),
        ),
    ]
