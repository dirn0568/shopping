from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import Self_data
from mainapp.forms import Self_create_form
from mainapp.models import Self_create_shop
from shop_divisionapp.forms import Create_clothes_choice_option_size, \
    Create_clothes_choice_option_title, Create_clothes_choice_option_color, Create_clothes_choice_option_number
from shop_divisionapp.models import Clothes_option_detail_size, Clothes_option_title, \
    Clothes_option_size, Clothes_option_detail_title, Clothes_option_color, Clothes_option_order_detail


def mainnet(request):
    context = {}
    if Self_data.objects.last():
        data = Self_data.objects.last()
        context['data_pk'] = data.self_pk
    context['샵목록'] = Self_create_shop.objects.all()
    # for mbti in data:
    #     print(mbti.self_pk, '33333333333333333333')
    #     context['data_pk'] = mbti.self_pk

    return render(request, 'mainpage.html', context)

def create_shop(request):
    if request.method == "POST":
        print(request.POST, '새로추가!@#%!%!#%!#%!#%!#%$!$@!')
        form = Self_create_form(request.POST, request.FILES)
        form2 = Create_clothes_choice_option_title(request.POST)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
        else:
            raise Http404("옷제작이 되지않았습니다")
        return redirect('mainapp:main')
    context={}
    context['샵생성'] = Self_create_form
    context['샵목록지정'] = Create_clothes_choice_option_title
    return render(request, 'create_shop.html', context)

def detail_shop(request, pk):
    shop_url = Self_create_shop.objects.filter(pk=pk)
    context = {}
    for mbti in shop_url:
        context['옷이미지'] = mbti.shop_img.url
        context['옷이름'] = mbti.shop_name
        context['옷가격'] = mbti.shop_cash
        context['shop_pk'] = mbti.pk
    return render(request, 'detail_shop.html', context)

def order_list(request):
    choice_user = Self_data.objects.last()
    choice_shop = Clothes_option_order_detail.objects.filter(clothes_order_pk=choice_user.self_data)
    print(choice_shop)
    context = {}
    context['옷주문'] = []
    for mbti in choice_shop:
        context['옷주문'].append(mbti)
    print(context['옷주문'], '345135132513531')
    return render(request, 'order_list.html', context)




