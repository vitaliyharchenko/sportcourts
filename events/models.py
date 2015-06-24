# coding=utf-8
from django.db import models
from customuser.models import User
from courts.models import Court

from utils.validators import gte_now


# Create your models here.
class SportType(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название вида спорта')

    class Meta():
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'

    def __unicode__(self):
        return self.title


class GameType(models.Model):
    sporttype = models.ForeignKey(SportType, verbose_name='Вид спорта')
    title = models.CharField(max_length=100, verbose_name='Название типа игры')

    class Meta():
        verbose_name = 'Тип игры'
        verbose_name_plural = 'Типы игры'

    def __unicode__(self):
        return u'{} - {}'.format(self.sporttype.title, self.title)


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    # TODO: add image of event

    # TODO: add status for public views

    # TODO: add event types
    # # Открытая игра
    # OPEN_GAME = 0
    # # Тренировка с тренером
    # PRACTICE = 1
    # # Соревнование личное
    # COMPETITION = 2
    # # Соревнование командное
    # TOURNAMENT = 2
    # type = models.IntegerField(default=OPEN_GAME, verbose_name='Тип события',
    #                              choices=())

    responsible_user = models.ForeignKey(User, related_name='responsible_games',
                                         limit_choices_to={'is_responsible': True},
                                         verbose_name='Ответственный')
    # auto define in admin.py
    created_by = models.ForeignKey(User)

    court = models.ForeignKey(Court, verbose_name='Площадка')

    gametype = models.ForeignKey(GameType, verbose_name='Тип игры')

    capacity = models.IntegerField(verbose_name='Вместимость')

    cost = models.PositiveIntegerField(verbose_name='Цена')

    #TODO: add validator until now
    datetime = models.DateTimeField(verbose_name='Дата проведения', validators=[gte_now])

    class Meta():
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __unicode__(self):
        return self.title


# class Game(Event):
#     reserved_count = models.PositiveIntegerField(verbose_name='Резервных мест', default=0)
#     deleted = models.BooleanField(default=False, verbose_name='Игра удалена')
#
#     subscribed = models.ManyToManyField(User, default=None, null=True,
#                                         blank=True, verbose_name='Участники', limit_choices_to={'is_active':True})
#     reserved = models.ManyToManyField(User, default=None, null=True, blank=True,
#                                       verbose_name='В резерве')
#
#     @property
#     def duration(self):
#         # TODO: result of decrease dates
#         return 120
#
#     class Meta:
#         ordering = ['-datetime']
#         get_latest_by = 'datetime'
#
#     def __unicode__(self):
#         return self.title
#
#     def delete(self, using=None):
#         # не забыть удалить все уведомления
#         # и отправить всем что игра удалена
#         return super(Game, self).delete(using)