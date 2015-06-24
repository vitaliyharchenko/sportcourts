# coding=utf-8
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)

    def __unicode__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)

    def __unicode__(self):
        return self.title


class Place(models.Model):
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    # долгота
    longitude = models.FloatField()
    # широта
    latitude = models.FloatField()
    fulladdress = models.CharField(max_length=500, verbose_name='Адрес', unique=True)

    def __unicode__(self):
        return self.fulladdress


class CourtType(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название типа площадки')

    def __unicode__(self):
        return self.title


class Cover(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название типа покрытия')

    def __unicode__(self):
        return self.title


class Worktime(models.Model):
    timefrom = models.TimeField(verbose_name='Начало работы')
    timeto = models.TimeField(verbose_name='Конец работы')

    def __unicode__(self):
        return u'с {} до {}'.format(self.timefrom, self.timeto)


class Court(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    description = models.CharField(max_length=300, verbose_name='Описание')
    admin_description = models.CharField(max_length=200, blank=True, verbose_name='Примечания для админов')
    place = models.ForeignKey(Place, verbose_name='Место')

    type = models.ForeignKey(CourtType, verbose_name='Тип площадки', related_name='+', null=True)
    # TODO: adding worktime and cover
    # worktime = models.ForeignKey(Worktime, verbose_name='Режим работы', blank=True, null=True)
    # cover = models.ForeignKey(Cover, verbose_name='Покрытие', blank=True, null=True)

    phone = PhoneNumberField(verbose_name='Телефон', help_text='В формате +7xxxxxxxxxx', blank=True)

    max_players = models.IntegerField(verbose_name='Максимальное количество игроков', default=0)

    cost = models.IntegerField(verbose_name='Стоимость аренды, RUB/час', default=0)
    # photo = JasnyImageModelField(upload_to='courts', verbose_name='Изображение', blank=True, null=True)
    # TODO: sporttypes
    # sporttypes = models.ManyToManyField('games.SportType', related_name='+', verbose_name='Типы спорта')
    # TODO: adding number of views

    def __unicode__(self):
        return self.title