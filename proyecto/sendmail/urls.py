# sendemail/urls.py
from django.contrib import admin

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^mail/', views.emailView, name='email'),
    url(r'^success/', views.successView, name='success'),
]