# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_api', '0006_auto_20160331_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='name',
            field=models.CharField(default=b'x', max_length=30),
        ),
    ]
