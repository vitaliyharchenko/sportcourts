from django.conf.urls import patterns, url

import views


urlpatterns = patterns('notifications',
                       url(r'^/read$', views.notification_read, name='read'),
                       url(r'^/delete$', views.notification_delete, name='delete'),
                       )