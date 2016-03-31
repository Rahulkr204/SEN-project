# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0003_auto_20160330_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_capacity',
            field=models.IntegerField(default=0),
        ),
    ]
