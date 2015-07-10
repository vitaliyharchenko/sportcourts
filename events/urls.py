# coding=utf-8
from django.conf.urls import patterns, url, include

import views


urlpatterns = patterns('events',
                       url('^events/$', views.events, name='list'),
                       url('^event/(?P<event_id>\d+)$', views.event, name='detail'),
                       url('^events/action$', views.eventaction, name='eventaction'),
                       )