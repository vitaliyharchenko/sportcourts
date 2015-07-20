# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0012_user_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.ForeignKey(verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True, to='courts.City', null=True),
        ),
    ]
