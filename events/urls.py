from django.conf.urls import patterns, url, include

import views


urlpatterns = patterns('events',
                       url('^events/$', views.events, name='list'),
                       url('^events/action/(?P<event_type>\w+)/(?P<action>\w+)/(?P<event_id>\d+)$', views.eventaction,
                           name='eventaction'),
                       )