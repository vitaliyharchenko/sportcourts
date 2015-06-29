from django.conf.urls import url, patterns
from . import views
from django.conf.urls import include

urlpatterns = patterns('',
                       url(r'^login/$', views.login, name="login"),
                       url(r'^logout/$', views.logout, name="logout"),
                       url(r'^reg/(?P<token>.{5,100})$', views.reg, name="reg"),
                       url(r'^activation/add_email$', views.add_email_activation, name='add_email_activation'),
                       url(r'^activation/verify_email/(?P<token>.{5,100})$', views.verify_email, name='verify_email'),

                       url(r'^users/$', views.userslist, name='users'),
                       url(r'^users/(?P<user_id>\d+)$', views.userdetail, name='user'),
                       )