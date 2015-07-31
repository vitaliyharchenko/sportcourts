"""sportcourts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from sportcourts import settings
from . import views
import customuser.urls
import courts.urls
import events.urls
import teams.urls
import finances.urls
import blog.urls
import notifications.urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index, name='index'),
                       url(r'^contacts$', views.contacts, name='contacts'),
                       url(r'^courts', include(courts.urls, 'courts')),
                       url(r'^teams', include(teams.urls, 'teams')),
                       url(r'^blog', include(blog.urls, 'blog')),
                       url(r'^', include(events.urls, 'events')),
                       url(r'^fin/', include(finances.urls, 'finances')),
                       url(r'^notifications', include(notifications.urls, 'notifications')),
                       ) + customuser.urls.urlpatterns

urlpatterns += patterns('',
                        (r"^media/(?P<path>.*)$", 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))

if settings.IS_PRODUCTION is True:
    urlpatterns += staticfiles_urlpatterns()