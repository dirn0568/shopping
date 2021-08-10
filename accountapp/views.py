from django.http import request, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from accountapp.forms import Self_userCreateForm, Self_userUpdateForm
from accountapp.models import Self_user


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
    # if Self_userCreateForm.is_valid(Self_userCreateForm):
    #     Self_userCreateForm.save()
    #     return super().Self_userCreateForm(Self_userCreateForm)

    # def form_valid(self, Self_userCreateForm):

    return render(request, 'create_user.html', context)

# class account_create(request):
#     def form_vaild(self, Self_userCreateForm):
#         Self_userCreateForm.save()
#
#     def get_success_url(self):
#         return reverse('mainapp:main')


# class test():
#     model = Self_user
#     form_class = Self_userCreateForm
#     template_name = 'create_user.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('mainapp')

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

def account_detail(request, pk):
    data = Self_user.objects.filter(pk=pk)
    for intp in data:
        context = {}
        context['data'] = data
        context['Nickname'] = intp.self_nickname
        context['data_pk'] = pk
    return render(request, 'detail_user.html', context)


