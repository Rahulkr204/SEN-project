# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0010_auto_20160413_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='truck_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='logistics_api.Truck', null=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='driver_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='logistics_api.Driver', null=True),
        ),
    ]
