
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('sighin/',views.sighinuser, name='sighinuser'),
    path('login/',views.loginuser, name='loginuser'),
    path('logout/',views.logoutuser, name='logoutuser')
]
