# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0009_auto_20160409_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='trip_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='waypoint',
        ),
        migrations.AddField(
            model_name='orders',
            name='add_contact_num',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='additional_info',
            field=models.CharField(default=b' ', max_length=360),
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(default=b' ', max_length=90),
        ),
        migrations.AddField(
            model_name='truck',
            name='driver_id',
            field=models.ForeignKey(default=0, to='logistics_api.Driver'),
        ),
        migrations.AddField(
            model_name='truck',
            name='truck_number',
            field=models.CharField(default=b' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='logistics_user',
            name='contact_num',
            field=models.BigIntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='logistics_user',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='truck',
            name='truck_id',
            field=models.IntegerField(default=0, serialize=False, primary_key=True),
        ),
    ]
