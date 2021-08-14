from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import Self_data
from mainapp.forms import Self_create_form, testing123
from mainapp.models import Self_create_shop
from shop_divisionapp.forms import Create_clothes_choice_option_size, Create_clothes_choice_option_size_testing
from shop_divisionapp.models import Clothes_assemble, Clothes_choice, Clothes_option_detail_size, Clothes_option_title, \
    Clothes_option_size


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
        form = Self_create_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            raise Http404("옷제작이 되지않았습니다")
        return redirect('mainapp:main')
    context={}
    context['샵생성'] = Self_create_form
    return render(request, 'create_shop.html', context)

def detail_shop(request, pk):
    shop_url = Self_create_shop.objects.filter(pk=pk)
    clothes_title = Clothes_option_title.objects.first()
    clothes_choice = Clothes_option_size.objects.filter(clothes_option_parent=clothes_title)
    context = {}
    # test222 = []
    # print(test222)
    form = Create_clothes_choice_option_size_testing
    # form.Meta.fields.append(test222)
    for mbti in clothes_choice:
        if form.Meta.fields.count(mbti.clothes_size) == 0:
            form.Meta.fields.append(mbti.clothes_size)
    # form.Meta.fields.test222.save()
    print(form.Meta.fields)
    # for mbti in clothes_choice:
    #     form.Meta.fields.test222.save(mbti)
    # form.Meta.fields.test222 = clothes_choice
    # for mbti in clothes_choice:
    #     form.Meta.fields.clothes_option_detail = mbti
    # for mbti in clothes_choice:
    #     context['test'] = mbti.clothes_size
    # print(form.Meta.fields['clothes_option_detail'], '33333333333333333333')
    # print(form.Meta.fields.test222, '33333333333333333333')
    context['test'] = form.Meta.fields

    testing = testing123

    for mbti in shop_url:
        context['옷이미지'] = mbti.shop_img.url
        context['옷이름'] = mbti.shop_name
        context['옷가격'] = mbti.shop_cash
        context['shop_pk'] = mbti.pk
        context['clothes_choice_list'] = 'Create_clothes_choice_option_size_testing'
    return render(request, 'detail_shop.html', context)




