from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import Self_data
from mainapp.forms import Self_create_form
from mainapp.models import Self_create_shop


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
    context={}
    for mbti in shop_url:
        context['옷이미지'] = mbti.shop_img.url
        context['옷이름'] = mbti.shop_name
        context['옷가격'] = mbti.shop_cash
    return render(request, 'detail_shop.html', context)




