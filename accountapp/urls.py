
from django.contrib import admin
from django.urls import path, include

from accountapp import views
# from accountapp.views import account_create

app_name = 'accountapp'

urlpatterns = [
    path('create/', views.account_create, name='account_create'),
    path('detail/<int:pk>', views.account_detail, name='account_detail'),
    path('update/<int:pk>', views.account_update, name='account_update'),
    path('delete/<int:pk>', views.account_delete, name='account_delete'),

    path('login', views.account_login, name='account_login'),
    path('logout', views.account_logout, name='account_logout'),



    # path('create/', account_create.as_view(), name='account_create'),
]
