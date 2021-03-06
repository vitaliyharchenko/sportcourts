# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import utils.witgets
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'Email', db_index=True)),
                ('is_active', models.BooleanField(default=True, help_text=b'\xd0\xa1\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb5 \xd0\xbd\xd0\xb5\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xb2\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xbe \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb0\xd0\xba\xd0\xba\xd0\xb0\xd1\x83\xd0\xbd\xd1\x82\xd0\xb0', verbose_name=b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('is_referee', models.BooleanField(default=False, help_text=b'\xd0\x9c\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82 \xd1\x81\xd1\x83\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b', verbose_name=b'\xd0\xa1\xd1\x83\xd0\xb4\xd1\x8c\xd1\x8f')),
                ('is_coach', models.BooleanField(default=False, help_text=b'\xd0\x9c\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82 \xd0\xb2\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8 \xd1\x82\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8', verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb5\xd1\x80')),
                ('is_responsible', models.BooleanField(default=False, help_text=b'\xd0\x97\xd0\xb0\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd1\x8f\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x82\xd1\x87\xd0\xb5\xd1\x82\xd1\x8b, \xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x80\xd1\x83\xd0\xb5\xd1\x82 \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9')),
                ('is_organizer', models.BooleanField(default=False, help_text=b'\xd0\xa1\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b, \xd0\xbf\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb8, \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85', verbose_name=b'\xd0\x9e\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80')),
                ('is_admin', models.BooleanField(default=False, help_text=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb2, \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82 \xd1\x81 \xd0\xb7\xd0\xb0\xd1\x80\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xb8 \xd0\xb1\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xb4\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85', verbose_name=b'\xd0\x90\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd')),
                ('is_staff', models.BooleanField(default=False, help_text=b'\xd0\x9e\xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8f\xd0\xb5\xd1\x82 , \xd0\xbc\xd0\xbe\xd0\xb6\xd0\xb5\xd1\x82 \xd0\xbb\xd0\xb8 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xb9\xd1\x82\xd0\xb8 \xd0\xb2 \xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xba\xd1\x83', verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81 \xd1\x81\xd0\xbe\xd1\x82\xd1\x80\xd1\x83\xd0\xb4\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0')),
                ('banned', models.BooleanField(default=False, help_text=b'\xd0\xa1\xd1\x82\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82 \xd0\xb1\xd0\xb0\xd0\xbd \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8e', verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd')),
                ('avatar', utils.witgets.JasnyImageModelField(upload_to=b'avatars', null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('bdate', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('first_name', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('last_name', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('vkuserid', models.IntegerField(unique=True, null=True, blank=True)),
                ('sex', models.CharField(max_length=1, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'm', b'\xd0\xbc\xd1\x83\xd0\xb6.'), (b'f', b'\xd0\xb6\xd0\xb5\xd0\xbd.')])),
                ('phone', utils.witgets.MyPhoneField(unique=True, max_length=128, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('weight', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\x92\xd0\xb5\xd1\x81', validators=[utils.validators.validate_weight])),
                ('height', models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xbe\xd1\x81\xd1\x82', validators=[utils.validators.validate_height])),
            ],
            options={
                'abstract': False,
                'verbose_name': '\u0418\u0433\u0440\u043e\u043a',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': '\u0418\u0433\u0440\u043e\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('email', models.EmailField(max_length=254, unique=True, serialize=False, verbose_name=b'Email', primary_key=True)),
                ('status', models.IntegerField(default=0, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81', choices=[(0, b'\xd0\xa1\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbe'), (1, b'\xd0\x9f\xd0\xbe\xd0\xb4\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xbe'), (2, b'\xd0\x97\xd0\xb0\xd1\x80\xd0\xb5\xd0\xb3\xd0\xb5\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd')])),
                ('token', models.CharField(unique=True, max_length=100, verbose_name=b'\xd0\x9a\xd0\xbb\xd1\x8e\xd1\x87 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
            ],
            options={
                'ordering': ['-datetime'],
                'verbose_name': '\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u0435 \u043f\u043e\u0447\u0442\u044b',
                'verbose_name_plural': '\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f \u043f\u043e\u0447\u0442\u044b',
            },
        ),
    ]
