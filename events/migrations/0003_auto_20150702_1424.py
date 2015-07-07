# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_game_is_reported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='is_reported',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd'),
        ),
    ]
