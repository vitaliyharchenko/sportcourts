# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0006_remove_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to=b'avatars', null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True),
        ),
    ]
