# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
        ('customuser', '0011_user_bdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(blank=True, to='courts.City', null=True),
        ),
    ]
