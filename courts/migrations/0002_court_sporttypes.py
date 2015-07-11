# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150710_1426'),
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='sporttypes',
            field=models.ManyToManyField(related_name='+', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf\xd1\x8b \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='events.SportType'),
        ),
    ]
