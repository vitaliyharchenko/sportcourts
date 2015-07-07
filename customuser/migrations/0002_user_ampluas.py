# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150702_1424'),
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ampluas',
            field=models.ManyToManyField(to='events.Amplua', verbose_name=b'\xd0\x90\xd0\xbc\xd0\xbf\xd0\xbb\xd1\x83\xd0\xb0'),
        ),
    ]
