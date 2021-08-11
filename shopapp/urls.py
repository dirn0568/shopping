from django.contrib import admin
from django.urls import path, include

from shopapp import views

app_name = 'shopapp'

urlpatterns = [
    path('shop_box/<int:pk>', views.shop_box, name='shop_box'),
    path('shop_list/<int:pk>', views.shop_list, name='shop_list'),
    path('shop_delete/<int:pk>', views.shop_delete, name='shop_delete'),
]