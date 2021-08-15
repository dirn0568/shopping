from django.contrib import admin
from django.urls import path, include

from shop_divisionapp import views

app_name = 'shop_divisionapp'

urlpatterns = [
    path('create_option', views.create_option, name='create_option'),
    path('create_option_size', views.create_option_size, name='create_option_size'),
]