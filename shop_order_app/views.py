from django.shortcuts import render, redirect

# Create your views here.
from mainapp.models import Self_create_shop
from shop_divisionapp.forms import Create_clothes_choice_option_size, Create_clothes_choice_option_color, \
    Create_clothes_choice_option_number
from shop_divisionapp.models import Clothes_option_detail_title, Clothes_option_size, Clothes_option_color


def order(request, pk):
    shop_url = Self_create_shop.objects.filter(pk=pk)
    clothes_title = Clothes_option_detail_title.objects.filter(pk=pk)
    for mbti in clothes_title:
        clothes_detail_title = mbti.clothes_option_detail_title
    clothes_choice = Clothes_option_size.objects.filter(clothes_option_size=clothes_detail_title)
    clothes_choice2 = Clothes_option_color.objects.filter(clothes_option_color=clothes_detail_title)
    context = {}
    form = Create_clothes_choice_option_size
    form2 = Create_clothes_choice_option_color
    form.Meta.fields = []
    form2.Meta.fields = []
    for mbti in clothes_choice:
        form.Meta.fields.append(mbti.clothes_size)
    for mbti in clothes_choice2:
        form2.Meta.fields.append(mbti.clothes_color)
    context['order_size'] = form.Meta.fields
    context['order_color'] = form2.Meta.fields
    context['order_number'] = Create_clothes_choice_option_number
    for mbti in shop_url:
        context['옷이미지'] = mbti.shop_img.url
        context['옷이름'] = mbti.shop_name
        context['옷가격'] = mbti.shop_cash
        context['shop_pk'] = mbti.pk
    return render(request, 'shop_order.html', context)

def check(request, pk):
    print(request.POST, '#!#%!#%!#%!#%!#')
    print(request.POST.submit, '#!#%!#%!#%!#%!#')
    return redirect('mainapp:main')
