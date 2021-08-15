from django.contrib import admin

# Register your models here.
from shop_divisionapp.models import Clothes_option_title, Clothes_option_size, \
    Clothes_option_detail_size, Clothes_option_detail_title, Clothes_option_color, Clothes_option_detail_color, \
    Clothes_option_number

# 주문 사항 양식
admin.site.register(Clothes_option_title)
admin.site.register(Clothes_option_size)
admin.site.register(Clothes_option_color)

# 세부 주문 사항
admin.site.register(Clothes_option_detail_title)
admin.site.register(Clothes_option_detail_size)
admin.site.register(Clothes_option_detail_color)
admin.site.register(Clothes_option_number)