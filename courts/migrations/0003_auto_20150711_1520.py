# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_court_sporttypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='views',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='sporttypes',
            field=models.ManyToManyField(to='events.SportType', verbose_name='\u0422\u0438\u043f\u044b \u0441\u043f\u043e\u0440\u0442\u0430', blank=True),
        ),
    ]
