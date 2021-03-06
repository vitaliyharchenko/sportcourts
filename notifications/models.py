# coding=utf-8
from django.db import models
from customuser.models import User


# Create your models here.
class Notification(models.Model):
    INFO = 0
    WARNING = 1
    DANGER = 2

    NEW = 0
    READ = 1
    DELETE = 2

    user = models.ForeignKey(User, related_name='notifications', verbose_name='Пользователь')
    datetime = models.DateTimeField(verbose_name='Время')
    text = models.TextField(verbose_name='Текст')

    read = models.PositiveSmallIntegerField(default=0, choices=(
        (NEW, 'Новое'),
        (READ, 'Прочитаное'),
        (DELETE, 'Удаленное'),), verbose_name='Статус')

    level = models.PositiveSmallIntegerField(default=0, choices=(
        (INFO, 'Информация'),
        (WARNING, 'Обратите внимание'),
        (DANGER, 'Внимание'),), verbose_name='Уровень уведомления')

    class Meta:
        ordering = ['-datetime']
        get_latest_by = 'datetime'

    def __unicode__(self):
        return self.text