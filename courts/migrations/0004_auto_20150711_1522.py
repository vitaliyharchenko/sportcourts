# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0003_auto_20150711_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
