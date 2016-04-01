# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0005_auto_20160330_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='waypoint',
            field=models.CharField(max_length=360),
        ),
    ]
