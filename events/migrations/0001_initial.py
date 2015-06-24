# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import utils.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('description', models.CharField(max_length=300, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('capacity', models.IntegerField(verbose_name=b'\xd0\x92\xd0\xbc\xd0\xb5\xd1\x81\xd1\x82\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c')),
                ('cost', models.PositiveIntegerField(verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0')),
                ('datetime', models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', validators=[utils.validators.gte_now])),
                ('court', models.ForeignKey(verbose_name=b'\xd0\x9f\xd0\xbb\xd0\xbe\xd1\x89\xd0\xb0\xd0\xb4\xd0\xba\xd0\xb0', to='courts.Court')),
                ('created_by', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb8\xd0\xbf\xd0\xb0 \xd0\xb8\xd0\xb3\xd1\x80\xd1\x8b')),
            ],
        ),
        migrations.CreateModel(
            name='SportType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2\xd0\xb8\xd0\xb4\xd0\xb0 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0')),
            ],
        ),
        migrations.AddField(
            model_name='gametype',
            name='sporttype',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd1\x81\xd0\xbf\xd0\xbe\xd1\x80\xd1\x82\xd0\xb0', to='events.SportType'),
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
    ]
