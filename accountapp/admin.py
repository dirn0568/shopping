from django.contrib import admin

# Register your models here.

from .models import Self_user, Self_data

admin.site.register(Self_user)
admin.site.register(Self_data)

