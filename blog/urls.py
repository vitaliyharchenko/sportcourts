# coding=utf-8
from django.conf.urls import patterns, url, include

import views


urlpatterns = patterns('blog',
                       url('^$', views.index, name='index'),
                       )