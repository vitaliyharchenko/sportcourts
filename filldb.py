# coding=utf-8
import sys
import os

import django


sys.path.extend(['/Dev/sportcourts'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sportcourts.settings")
django.setup()

from courts.models import Court, Place, City, Country, CourtType
from events.models import SportType, GameType, Game
from customuser.models import User

# print 'Creating superuser...'
# User.objects.create_superuser(email="harchenko.grape@gmail.com", password="4203", first_name="Vitaliy",
#                               last_name="Harchenko")
#
# print 'Creating places...'
# Country.objects.create(title=u'Россия')
# City.objects.create(title=u'Екатеринбург')
# City.objects.create(title=u'Москва')
# CourtType.objects.create(title=u'Крытая')
# CourtType.objects.create(title=u'Открытая')
# Place.objects.create(country=Country.objects.get(title=u'Россия'), city=City.objects.get(title=u'Екатеринбург'),
#                      longitude=60.0, latitude=60.0, fulladdress=u'Техническая 16а')
# Place.objects.create(country=Country.objects.get(title=u'Россия'), city=City.objects.get(title=u'Екатеринбург'),
#                      longitude=62.0, latitude=62.0, fulladdress=u'Гражданская 2')
#
#
# print 'Creating courts...'
# Court.objects.create(title=u'ФОК Железнодорожный', description=u'Первый наш зал, йоу!',
#                      place=Place.objects.get(fulladdress=u'Техническая 16а'), type=CourtType.objects.get(title=u'Крытая'),
#                      phone='+79826469454', max_players=10, cost=1000)
# Court.objects.create(title=u'Второй зал', description=u'второй наш зал, йоу!',
#                      place=Place.objects.get(fulladdress=u'Гражданская 2'), type=CourtType.objects.get(title=u'Открытая'),
#                      phone='+79826469455', max_players=15, cost=2000)
# print Court.objects.all()
#
#
# print 'Creating sport types...'
# SportType.objects.create(title=u'Баскетбол')
# SportType.objects.create(title=u'Волейбол')


print 'Creating game types...'
GameType.objects.create(title=u'Открытая игра 5х5', sporttype=SportType.objects.get(title=u'Баскетбол'))
GameType.objects.create(title=u'Стритбол 3х3', sporttype=SportType.objects.get(title=u'Баскетбол'))