from django.http import request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from accountapp.forms import Self_userCreateForm
from accountapp.models import Self_user


# class CreateAccountView(CreateView):
#     model = Self_user
#     form_class =
#     template_name =

def account(request):
    if request.method == "POST":
        form = Self_userCreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('안됐음')

        # form = Self_userCreateForm
        # print(form)
        # form.save()
        return render(request, 'mainpage.html')
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

def test2(requeset):
    Self_user(self_name='test7891011', self_password=1234, self_nickname='똒띠띠띠띠EL').save()
    context={}
    return render(request, 'create_user.html', context)


