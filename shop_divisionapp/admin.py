from django.contrib import admin

# Register your models here.
from shop_divisionapp.models import Clothes_assemble, Clothes_choice, Clothes_option_title, Clothes_option_size, \
    Clothes_option_detail_size

admin.site.register(Clothes_assemble)
admin.site.register(Clothes_choice)
admin.site.register(Clothes_option_title)
admin.site.register(Clothes_option_size)



admin.site.register(Clothes_option_detail_size)