from django.contrib import admin
from django.urls import path, include

from mainapp import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.mainnet, name='main'),
    path('main_option/<word>', views.mainnet_option, name='main_option'),

    path('create_shop', views.create_shop, name='create_shop'),
    path('detail_shop/<int:pk>', views.detail_shop, name='detail_shop'),
    path('order_list', views.order_list, name='order_list'),
]