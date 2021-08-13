from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/', include('mainapp.urls')),
    path('account/', include('accountapp.urls')),
    path('shop/', include('shopapp.urls')),
    path('shop_division/', include('shop_divisionapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
