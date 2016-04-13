# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0008_auto_20160403_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truck',
            name='remaining_capacity',
        ),
        migrations.AddField(
            model_name='driver',
            name='attendance',
            field=models.CharField(default=b'absent', max_length=20),
        ),
        migrations.AddField(
            model_name='trip',
            name='status',
            field=models.CharField(default=b'InTransit', max_length=20),
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_status',
            field=models.CharField(default=b'InGarage', max_length=20),
        ),
    ]
