from django.contrib import admin
from django.urls import path, include

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('start', views.test, name='main'),
]