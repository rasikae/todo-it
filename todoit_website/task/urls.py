from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
   path('home', views.home, name='home'),
   path('', views.login, name='login'),
]

