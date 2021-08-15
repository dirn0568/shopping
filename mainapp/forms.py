from django.forms import ModelForm

from mainapp.models import Self_create_shop



class Self_create_form(ModelForm):
    class Meta:
        model = Self_create_shop
        fields = ['shop_img', 'shop_name', 'shop_cash']

