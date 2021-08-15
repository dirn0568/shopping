from django.forms import ModelForm

from shop_divisionapp.models import Clothes_option_title, Clothes_option_size, \
    Clothes_option_detail_size, Clothes_option_detail_title, Clothes_option_color, Clothes_option_detail_color, \
    Clothes_option_number


class Create_clothes_choice_title(ModelForm):
    class Meta:
        model = Clothes_option_title
        fields = ['clothes_title']

class Create_clothes_choice_option_title(ModelForm):
    class Meta:
        model = Clothes_option_detail_title
        fields = ['clothes_option_detail_title']

class Create_clothes_choice_option_color(ModelForm):
    class Meta:
        model = Clothes_option_color
        fields = ['clothes_option_color', 'clothes_color']

class Create_clothes_choice_option_size(ModelForm):
    class Meta:
        model = Clothes_option_detail_size
        fields = []
class Create_clothes_choice_option_color(ModelForm):
    class Meta:
        model = Clothes_option_detail_color
        fields = []
class Create_clothes_choice_option_number(ModelForm):
    class Meta:
        model = Clothes_option_number
        fields = ['order_number']
