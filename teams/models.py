# coding=utf-8
from django.db import models


# Create your models here.
class Team(models.Model):

    class Meta:
        verbose_name = 'команда'
        verbose_name_plural = 'команды'
        app_label = 'teams'

    title = models.CharField(max_length=100, verbose_name='Название команды')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/teams/%i" % self.id


class UserTeam(models.Model):

    class Meta():
        verbose_name = 'членство в команде'
        verbose_name_plural = 'членства в команде'
        app_label = 'teams'

    user = models.ForeignKey('customuser.User', verbose_name='Пользователь')
    team = models.ForeignKey(Team, verbose_name='Команда')
    amplua = models.ForeignKey('events.Amplua', verbose_name='Амплуа')
    datetime = models.DateTimeField(verbose_name='Дата вступления', auto_now=True)

    def __unicode__(self):
        return u'{} | {} | {}'.format(self.user, self.team, self.amplua)