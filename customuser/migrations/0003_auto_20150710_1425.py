# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_user_ampluas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ampluas',
            field=models.ManyToManyField(to='events.Amplua', verbose_name='\u0410\u043c\u043f\u043b\u0443\u0430'),
        ),
    ]
