# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0007_auto_20160331_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logistics_user',
            fields=[
                ('contact_num', models.IntegerField(default=0, serialize=False, primary_key=True)),
                ('email_id', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='orders',
            name='date',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='trip_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='user_id',
        ),
        migrations.AddField(
            model_name='driver',
            name='trip_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='logistics_api.Trip', null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='orders',
            name='contact_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='logistics_api.Logistics_user', null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='logistics_api.Orders', null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
