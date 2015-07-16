# coding=utf-8
from django.db import models
from customuser import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Заголовок')
    author = models.ForeignKey(User, verbose_name=u'Автор', null=True, blank=True)

    def __unicode__(self):
        return self.title
