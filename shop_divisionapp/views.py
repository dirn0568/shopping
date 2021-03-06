from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from shop_divisionapp.forms import Create_clothes_choice_option_size, Create_clothes_choice_title



def create_option(request):
    if request.method == "POST":
        form = Create_clothes_choice_title(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Http404("clothes_option 선택이 되지않았습니다")
        return redirect('mainapp:main')
    context={}
    context['create_option'] = Create_clothes_choice_title
    return render(request, 'create_option.html', context)

def create_option_size(request):
    if request.method == "POST":
        form = Create_clothes_choice_option_size(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Http404("clothes_option_size 사이즈가 선택되지않았습니다")
        return redirect('mainapp:main')
    context={}
    context['create_option_size'] = Create_clothes_choice_option_size
    return render(request, 'create_option_size.html', context)