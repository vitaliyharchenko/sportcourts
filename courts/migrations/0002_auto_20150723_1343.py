# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='sporttypes',
            field=models.ManyToManyField(to='events.SportType', verbose_name='\u0422\u0438\u043f\u044b \u0441\u043f\u043e\u0440\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='court',
            name='type',
            field=models.ForeignKey(related_name='+', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbf\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb8', to='courts.CourtType', null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(to='courts.Region'),
        ),
    ]
