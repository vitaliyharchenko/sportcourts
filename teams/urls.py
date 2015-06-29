from django.conf.urls import url, patterns
from views import *

urlpatterns = patterns('teams',
                       url(r'^$', teamslist, name='list'),
                       url(r'^(?P<team_id>\d+)$', teamdetail, name='detail'),
                       )