# coding=utf-8
from django.conf.urls import patterns, url, include

import views


urlpatterns = patterns('events',
                       url('^events/$', views.events, name='list'),
                       url('^events/action$', views.eventaction, name='eventaction'),
                       )