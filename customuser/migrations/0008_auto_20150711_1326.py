# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0007_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xbe\xd1\x81\xd1\x82', validators=[utils.validators.validate_height]),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\x92\xd0\xb5\xd1\x81', validators=[utils.validators.validate_weight]),
        ),
    ]
