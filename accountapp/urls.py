
from django.contrib import admin
from django.urls import path, include

from accountapp import views
# from accountapp.views import account_create

app_name = 'accountapp'

urlpatterns = [
    path('create/', views.account, name='create'),
    path('detail/<int:pk>', views.test, name='detail'),

    path('test/', views.test2, name='test2'),
    # path('create/', account_create.as_view(), name='account_create'),
]
