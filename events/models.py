# coding=utf-8
from django.db import models
from customuser.models import User
from courts.models import Court
from django.contrib.contenttypes.models import ContentType

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

    # определяет класс дочерней модели
    content_type = models.ForeignKey(ContentType, editable=False, null=True)

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

    datetime = models.DateTimeField(verbose_name='Дата проведения', validators=[gte_now])
    datetime_to = models.DateTimeField(verbose_name='Дата окончания', validators=[gte_now], blank=True)

    class Meta():
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-datetime']
        get_latest_by = 'datetime'

    def __unicode__(self):
        return self.title

    # then save, define class of children class
    def save(self):
        if not self.content_type:
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        self.save_base()

    # then we can return object as one of children class objects
    def as_leaf_class(self):
        content_type = self.content_type
        model = content_type.model_class()
        if model == Event:
            return self
        return model.objects.get(id=self.id)


class Game(Event):
    reserved_count = models.PositiveIntegerField(verbose_name='Резервных мест', default=0)
    deleted = models.BooleanField(default=False, verbose_name='Игра удалена')

    # default=None, null=True, blank=True, verbose_name='Участники', limit_choices_to={'is_active':True}
    reserved = models.ManyToManyField(User, related_name='reserved_games', blank=True)

    # может быть, а может и не быть тренер на игре
    coach = models.ForeignKey(User, related_name='coach', blank=True, null=True)

    @property
    def subscribed(self):
        actions = UserGameAction.objects.filter(game=self).filter(action=UserGameAction.SUBSCRIBED)
        users = list()
        for action in actions:
            users.append(action.user)
        return users

    @property
    def duration(self):
        # TODO: beautiful format of duration
        return self.datetime_to - self.datetime

    class Meta():
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __unicode__(self):
        return self.title

    # TODO: логика удаления игры
    # def delete(self, using=None):
    #     # не забыть удалить все уведомления
    #     # и отправить всем что игра удалена
    #     return super(Game, self).delete(using)


class UserGameAction(models.Model):

    class Meta():
        verbose_name = 'запись на игру'
        verbose_name_plural = 'записи на игру'

    SUBSCRIBED = 1
    UNSUBSCRIBED = 2
    RESERVED = 3
    UNRESERVED = 4
    ACTIONS = (
        (SUBSCRIBED, 'Записался'),
        (UNSUBSCRIBED, 'Отписался'),
        (RESERVED, 'В резерве'),
        (UNRESERVED, 'Вышел из резерва')
    )
    user = models.ForeignKey(User, verbose_name='Пользователь')
    game = models.ForeignKey(Game, verbose_name='Игра')
    datetime = models.DateTimeField(verbose_name='Дата действия', auto_now=True)
    action = models.PositiveSmallIntegerField(verbose_name='Действие', choices=ACTIONS)

    def __unicode__(self):
        return u'{} {} {} {}'.format(self.game.id, self.game, self.user, self.action)


# TODO: model для турнира
# TODO: model для турнира
# TODO: model для турнира
# TODO: model для турнира