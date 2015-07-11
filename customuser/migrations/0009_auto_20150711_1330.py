# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0008_auto_20150711_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default=1, max_length=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'm', b'\xd0\x9c'), (b'f', b'\xd0\x96')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='vkuserid',
            field=models.IntegerField(unique=True, null=True, blank=True),
        ),
    ]
