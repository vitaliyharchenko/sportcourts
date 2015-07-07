# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0433\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '\u0433\u043e\u0440\u043e\u0434\u0430',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0441\u0442\u0440\u0430\u043d\u0430',
                'verbose_name_plural': '\u0441\u0442\u0440\u0430\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=300, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('admin_description', models.CharField(max_length=200, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbc\xd0\xb5\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xbe\xd0\xb2', blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text=b'\xd0\x92 \xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5 +7xxxxxxxxxx', max_length=128, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', blank=True)),
                ('max_players', models.IntegerField(default=0, verbose_name=b'\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe \xd0\xb8\xd0\xb3\xd1\x80\xd0\xbe\xd0\xba\xd0\xbe\xd0\xb2')),
                ('cost', models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xb0\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4\xd1\x8b, RUB/\xd1\x87\xd0\xb0\xd1\x81')),
            ],
            options={
                'verbose_name': '\u043f\u043b\u043e\u0449\u0430\u0434\u043a\u0430',
                'verbose_name_plural': '\u043f\u043b\u043e\u0449\u0430\u0434\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='CourtType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf\xd0\xb0 \xd0\xbf\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb8')),
            ],
            options={
                'verbose_name': '\u0442\u0438\u043f \u043f\u043b\u043e\u0449\u0430\u0434\u043a\u0438',
                'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043f\u043b\u043e\u0449\u0430\u0434\u043e\u043a',
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xba\xd1\x80\xd1\x8b\xd1\x82\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0442\u0438\u043f \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u044f',
                'verbose_name_plural': '\u0442\u0438\u043f\u044b \u043f\u043e\u043a\u0440\u044b\u0442\u0438\u0439',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('fulladdress', models.CharField(unique=True, max_length=500, verbose_name=b'\xd0\x90\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81')),
                ('city', models.ForeignKey(to='courts.City')),
            ],
            options={
                'verbose_name': '\u043c\u0435\u0441\u0442\u043e',
                'verbose_name_plural': '\u043c\u0435\u0441\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('country', models.ForeignKey(to='courts.Country')),
            ],
            options={
                'verbose_name': '\u043e\u0431\u043b\u0430\u0441\u0442\u044c',
                'verbose_name_plural': '\u043e\u0431\u043b\u0430\u0441\u0442\u0438',
            },
        ),
        migrations.CreateModel(
            name='Worktime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timefrom', models.TimeField(verbose_name=b'\xd0\x9d\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
                ('timeto', models.TimeField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x86 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b')),
            ],
        ),
        migrations.AddField(
            model_name='court',
            name='place',
            field=models.ForeignKey(verbose_name=b'\xd0\x9c\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe', to='courts.Place'),
        ),
        migrations.AddField(
            model_name='court',
            name='type',
            field=models.ForeignKey(related_name='+', verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbf\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb8', to='courts.CourtType', null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(to='courts.Region'),
        ),
    ]
