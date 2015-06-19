from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('courts',
                       url('^$', courtlist, name='courts'),
                       )