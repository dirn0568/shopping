
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/', include('mainapp.urls')),
    path('account/', include('accountapp.urls')),
]
