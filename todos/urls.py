
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
]
