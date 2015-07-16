# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20150710_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_public',
            field=models.BooleanField(default=True, help_text=b'\xd0\x94\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb8\xd0\xbc\xd1\x8b\xd0\xbc \xd0\xb2 \xd0\xbf\xd0\xbe\xd1\x82\xd0\xbe\xd0\xba\xd0\xb5', verbose_name=b'\xd0\x9f\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81'),
        ),
    ]
