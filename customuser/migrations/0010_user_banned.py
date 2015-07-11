# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0009_auto_20150711_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='banned',
            field=models.BooleanField(default=False, help_text=b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82 \xd0\xb1\xd0\xb0\xd0\xbd \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8e', verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd'),
        ),
    ]
