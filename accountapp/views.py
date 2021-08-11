from django.contrib.auth.models import User
from django.http import request, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from accountapp.forms import Self_userCreateForm, Self_userUpdateForm, Self_userLoginForm
from accountapp.models import Self_user, Self_data


def account_create(request):
    if request.method == "POST":
        form = Self_userCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
        else:
            raise Http404("회원가입이 되지않았습니다")
        Self_last = Self_user.objects.last()
        for entp in Self_user.objects.filter(pk = Self_last.pk):
            return redirect('accountapp:account_detail', entp.pk)
    context = {}
    context['회원가입'] = Self_userCreateForm

    return render(request, 'create_user.html', context)

def account_detail(request, pk):
    data = Self_user.objects.filter(pk=pk)
    for intp in data:
        context = {}
        context['data'] = data
        context['Nickname'] = intp.self_nickname
        context['data_pk'] = pk
    return render(request, 'detail_user.html', context)

def account_update(request, pk):
    # Self_user(self_name='test7891011', self_password=1234, self_nickname='똒띠띠띠띠EL').save()
    if request.method == "POST":
        name = request.POST['self_name']
        nickname = request.POST['self_nickname']
        if Self_user.objects.filter(self_name = name) or Self_user.objects.filter(self_nickname = nickname):
            raise Http404("변경이 되지않았습니다")
        for entp in Self_user.objects.filter(pk = pk):
            entp.self_name = name
            entp.self_nickname = nickname
            entp.save()
            return redirect('accountapp:account_detail', entp.pk)
    context={}
    context['개인정보수정'] = Self_userUpdateForm
    context['data_pk'] = pk
    return render(request, 'update_user.html', context)

def account_delete(request, pk):
    if request.method == "POST":
        for entp in Self_user.objects.filter(pk = pk):
            entp.delete()
            return redirect('mainapp:main')
    context={}
    context['data_pk'] = pk
    return render(request, 'delete_user.html', context)

def account_login(request):
    if request.method == "POST":
        name = request.POST['self_name']
        password = request.POST['self_password']
        if Self_user.objects.filter(self_name = name) and Self_user.objects.filter(self_password = password):
            for mbti in Self_user.objects.filter(self_name = name):
                intp = mbti.pk
                entp = mbti
            Self_data(self_data=entp, self_name=name, self_password=password, self_pk=intp).save()
            return redirect('mainapp:main')
    context = {}
    context['로그인'] = Self_userLoginForm
    return render(request, 'login_user.html', context)

def account_logout(request):
    data = Self_data.objects.last()
    for mbti in Self_data.objects.filter(pk=data.pk):
        mbti.delete()
    # last문은 for이 안돼???????
    return redirect('mainapp:main')




