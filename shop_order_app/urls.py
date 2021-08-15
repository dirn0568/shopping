from django.contrib import admin
from django.urls import path, include

from shop_order_app import views

app_name = 'shop_order_app'

urlpatterns = [
    path('order_page/<int:pk>', views.order, name='order_page'),
    path('order_check/<int:pk>', views.check, name='order_ckeck'),
]