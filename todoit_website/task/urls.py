from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
   path('home', views.home, name='home'),
   path('', views.login, name='login'),
   url(r'^home/(?P<project>.*)/$', views.home2, name='projecthome'),
   url(r'^home/(?P<delete>.*)/(?P<name>.*)/$', views.home, name='delete'),
]

