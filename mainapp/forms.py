from django.forms import ModelForm

from mainapp.models import Self_create_shop
from shop_divisionapp.models import Clothes_choice


class Self_create_form(ModelForm):
    class Meta:
        model = Self_create_shop
        fields = ['shop_img', 'shop_name', 'shop_cash']

class testing123(ModelForm):
    class Meta:
        model = Clothes_choice
        fields = ['clothes_choice_title', 'clothes_choice_size', 'clothes_choice_color']