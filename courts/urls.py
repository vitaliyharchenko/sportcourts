from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('courts',
                       url('^$', courtlist, name='list'),
                       url('^/(?P<court_id>\d+)$', court, name='detail'),
                       )