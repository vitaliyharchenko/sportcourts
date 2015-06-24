from django.conf.urls import patterns, url

import views


urlpatterns = patterns('events',
                       url('^events/$', views.events, name='list'),
                       )