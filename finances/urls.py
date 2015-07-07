from django.conf.urls import url, patterns
import views

urlpatterns = patterns('finances',
                       url(r'^$', views.fin, name='fin'),
                       )