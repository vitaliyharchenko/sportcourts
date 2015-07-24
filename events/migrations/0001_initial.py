# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amplua',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0430\u043c\u043f\u043b\u0443\u0430',
                'verbose_name_plural': '\u0430\u043c\u043f\u043b\u0443\u0430',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=300, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('is_public', models.BooleanField(default=True, help_text=b'\xd0\x94\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xb5\xd1\x82 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb8\xd0\xbc\xd1\x8b\xd0\xbc \xd0\xb2 \xd0\xbf\xd0\xbe\xd1\x82\xd0\xbe\xd0\xba\xd0\xb5', verbose_name=b'\xd0\x9f\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x83\xd1\x81')),
                ('capacity', models.IntegerField(verbose_name=b'\xd0\x92\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('cost', models.PositiveIntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('datetime', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('datetime_to', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd0\xba\xd0\xbe\xd0\xbd\xd1\x87\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
            ],
            options={
                'ordering': ['-datetime'],
                'get_latest_by': 'datetime',
                'verbose_name': '\u0421\u043e\u0431\u044b\u0442\u0438\u0435',
                'verbose_name_plural': '\u0421\u043e\u0431\u044b\u0442\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf\xd0\xb0 \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0438\u0433\u0440\u044b',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0438\u0433\u0440\u044b',
            },
        ),
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0412\u0438\u0434 \u0441\u043f\u043e\u0440\u0442\u0430',
                'verbose_name_plural': '\u0412\u0438\u0434\u044b \u0441\u043f\u043e\u0440\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='UserGameAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd1\x8f')),
                ('action', models.PositiveSmallIntegerField(verbose_name=b'\xd0\x94\xd0\xb5\xd0\xb9\xd1\x81\xd1\x82\xd0\xb2\xd0\xb8\xd0\xb5', choices=[(1, b'\xd0\x97\xd0\xb0\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbb\xd1\x81\xd1\x8f'), (2, b'\xd0\x9e\xd1\x82\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbb\xd1\x81\xd1\x8f'), (3, b'\xd0\x92 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb5'), (4, b'\xd0\x92\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbb \xd0\xb8\xd0\xb7 \xd1\x80\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb0'), (5, b'\xd0\x9f\xd0\xbe\xd1\x81\xd0\xb5\xd1\x82\xd0\xb8\xd0\xbb'), (6, b'\xd0\x9d\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb8\xd1\x88\xd0\xb5\xd0\xbb'), (7, b'\xd0\x9d\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xb8\xd0\xbb')])),
                ('user', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0437\u0430\u043f\u0438\u0441\u044c \u043d\u0430 \u0438\u0433\u0440\u0443',
                'verbose_name_plural': '\u0437\u0430\u043f\u0438\u0441\u0438 \u043d\u0430 \u0438\u0433\u0440\u0443',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('reserved_count', models.PositiveIntegerField(default=0, verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xb7\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbc\xd0\xb5\xd1\x81\xd1\x82')),
                ('deleted', models.BooleanField(default=False, verbose_name=b'\xd0\x98\xd0\xb3\xd1\x80\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('is_reported', models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x82 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd')),
                ('coach', models.ForeignKey(related_name='coach', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u0438\u0433\u0440\u0430',
                'verbose_name_plural': '\u0438\u0433\u0440\u044b',
            },
            bases=('events.event',),
        ),
        migrations.AddField(
            model_name='gametype',
            name='sporttype',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='events.SportType'),
        ),
        migrations.AddField(
            model_name='event',
            name='content_type',
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='court',
            field=models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb0', to='courts.Court'),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='gametype',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b', to='events.GameType'),
        ),
        migrations.AddField(
            model_name='event',
            name='responsible_user',
            field=models.ForeignKey(related_name='responsible_games', verbose_name=b'\xd0\x9e\xd1\x82\xd0\xb2\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amplua',
            name='sporttype',
            field=models.ForeignKey(related_name='+', verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='events.SportType'),
        ),
        migrations.AddField(
            model_name='usergameaction',
            name='game',
            field=models.ForeignKey(verbose_name=b'\xd0\x98\xd0\xb3\xd1\x80\xd0\xb0', to='events.Game'),
        ),
    ]
