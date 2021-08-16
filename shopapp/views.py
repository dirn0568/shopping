from django.shortcuts import render, redirect

# Create your views here.
from accountapp.models import Self_data, Self_user
from mainapp.models import Self_create_shop
from shopapp.models import Self_box


def shop_box(request, pk):
    box_data = Self_create_shop.objects.filter(pk=pk)
    box_data2 = Self_data.objects.last()
    box_data2 = Self_user.objects.filter(pk=box_data2.self_pk)
    for shop in box_data:
        for shop2 in box_data2:
            Self_box(self_box=shop2, box_img=shop.shop_img.url, box_name=shop.shop_name, box_cash=shop.shop_cash).save()
    return redirect('mainapp:detail_shop', pk=pk)

def shop_list(request, pk):
    user_obj = Self_user.objects.filter(pk=pk)
    for box_obj in user_obj:
        box_obj = Self_box.objects.filter(self_box=box_obj)
    for shop in box_obj:
        shop = Self_create_shop.objects.filter(shop_name=shop.box_name)
    for shop_pk in shop:
        shop_pk = shop_pk.pk
    print(box_obj)
    print(shop_pk)
    context={}
    context['장바구니'] = box_obj
    context['shop_pk'] = shop_pk
    return render(request, 'list_shop.html', context)

def shop_delete(request, pk):
    test2 = Self_data.objects.last()
    test = Self_box.objects.filter(pk=pk)
    test.delete()
    return redirect('shopapp:shop_list', pk=test2.self_pk)
