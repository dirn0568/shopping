from django.shortcuts import render

# Create your views here.
from accountapp.models import Self_data


def test(request):
    context = {}
    if Self_data.objects.last():
        data = Self_data.objects.last()
        context['data_pk'] = data.self_pk
    # for mbti in data:
    #     print(mbti.self_pk, '33333333333333333333')
    #     context['data_pk'] = mbti.self_pk

    return render(request, 'mainpage.html', context)

