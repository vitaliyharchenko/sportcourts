# coding=utf-8
from django.db import models
from customuser.models import User
from courts.models import Court
from django.contrib.contenttypes.models import ContentType

from utils.validators import gte_now
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError


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


class Amplua(models.Model):
    sporttype = models.ForeignKey(SportType, verbose_name='Вид спорта', related_name='+')
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta():
        verbose_name = 'амплуа'
        verbose_name_plural = 'амплуа'

    def __unicode__(self):
        return u'{} - {}'.format(self.sporttype.title, self.title)


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')

    # определяет класс дочерней модели
    content_type = models.ForeignKey(ContentType, editable=False, null=True)

    # TODO: add image of event
    # TODO: add status for public views
    # TODO: add working status for unclosed events

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
        if self.datetime > self.datetime_to:
            raise ValueError('Проверьте отрезки времени')
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

    @property
    def type(self):
        return self.content_type.model

    @property
    def duration(self):
        # TODO: beautiful format of duration
        return self.datetime_to - self.datetime

    @property
    def time_status(self):
        now = timezone.now()
        # считаем продоожительность события и высчитываем погрещнойсть для отображения статусов, аля "скоро начнется"
        if self.duration > datetime.timedelta(days=7):
            delta = datetime.timedelta(days=7)
        else:
            delta = self.duration

        # все возможные временные статусы события, влияющие на отображение
        if now <= self.datetime - delta:
            return 'WILL BE'
        elif now <= self.datetime:
            return 'COMING'
        elif now <= self.datetime_to:
            return 'IT GOES'
        else:
            return 'WAS'


class Game(Event):
    reserved_count = models.PositiveIntegerField(verbose_name='Резервных мест', default=0)
    deleted = models.BooleanField(default=False, verbose_name='Игра удалена')

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
    def reserved(self):
        actions = UserGameAction.objects.filter(game=self).filter(action=UserGameAction.RESERVED)
        users = list()
        for action in actions:
            users.append(action.user)
        return users

    @property
    def unsubscribed(self):
        actions = UserGameAction.objects.filter(game=self).exclude(action=UserGameAction.SUBSCRIBED).exclude(
            action=UserGameAction.RESERVED)
        users = list()
        for action in actions:
            users.append(action.user)
        return users

    @property
    def has_place(self):
        actions = UserGameAction.objects.filter(game=self).filter(action=UserGameAction.SUBSCRIBED)
        count = actions.count()
        if count >= self.capacity:
            return False
        else:
            return True

    @property
    def has_reserved_place(self):
        actions = UserGameAction.objects.filter(game=self).filter(action=UserGameAction.RESERVED)
        count = actions.count()
        if count >= self.reserved_count:
            return False
        else:
            return True

    class Meta():
        verbose_name = 'игра'
        verbose_name_plural = 'игры'

    def __unicode__(self):
        return self.title

        # TODO: логика удаления игры
        # def delete(self, using=None):
        # # не забыть удалить все уведомления
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
    VISITED = 5
    NOTVISITED = 6
    NOTPAY = 7
    ACTIONS = (
        (SUBSCRIBED, 'Записался'),
        (UNSUBSCRIBED, 'Отписался'),
        (RESERVED, 'В резерве'),
        (UNRESERVED, 'Вышел из резерва'),
        (VISITED, 'Посетил'),
        (NOTVISITED, 'Не пришел'),
        (NOTPAY, 'Не заплатил')
    )
    user = models.ForeignKey(User, verbose_name='Пользователь')
    game = models.ForeignKey(Game, verbose_name='Игра')
    datetime = models.DateTimeField(verbose_name='Дата действия', auto_now=True)
    action = models.PositiveSmallIntegerField(verbose_name='Действие', choices=ACTIONS)

    def __unicode__(self):
        return u'{} {} | {} | {}'.format(self.game.id, self.game, self.user, self.get_action_display())

    # TODO: проверка соответствия количеству мест при сохраниении

# TODO: model для турнира
# TODO: model для турнира
# TODO: model для турнира
# TODO: model для турнира