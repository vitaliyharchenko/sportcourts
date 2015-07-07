# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd1\x8b')),
            ],
            options={
                'verbose_name': '\u043a\u043e\u043c\u0430\u043d\u0434\u0430',
                'verbose_name_plural': '\u043a\u043e\u043c\u0430\u043d\u0434\u044b',
            },
        ),
        migrations.CreateModel(
            name='UserTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('amplua', models.ForeignKey(verbose_name=b'\xd0\x90\xd0\xbc\xd0\xbf\xd0\xbb\xd1\x83\xd0\xb0', to='events.Amplua')),
                ('team', models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xbd\xd0\xb4\xd0\xb0', to='teams.Team')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0447\u043b\u0435\u043d\u0441\u0442\u0432\u043e \u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u0435',
                'verbose_name_plural': '\u0447\u043b\u0435\u043d\u0441\u0442\u0432\u0430 \u0432 \u043a\u043e\u043c\u0430\u043d\u0434\u0435',
            },
        ),
    ]
