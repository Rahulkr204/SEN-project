# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('goods_type', models.CharField(max_length=30)),
                ('order_status', models.CharField(max_length=10)),
                ('trip_id', models.CharField(max_length=10)),
                ('quantity', models.CharField(max_length=10)),
                ('source', models.CharField(max_length=360)),
                ('destination', models.CharField(max_length=360)),
                ('date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('contact_num', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('trip_capacity', models.CharField(max_length=20)),
                ('waypoint', models.CharField(max_length=129600)),
                ('location', models.CharField(max_length=360)),
                ('order_id', models.ForeignKey(to='logistics_api.Orders')),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('truck_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('truck_capacity', models.CharField(max_length=20)),
                ('remaining_capacity', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='truck_id',
            field=models.ForeignKey(to='logistics_api.Truck'),
        ),
        migrations.AddField(
            model_name='trip',
            name='user_id',
            field=models.ForeignKey(to='logistics_api.User'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
