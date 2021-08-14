from django.forms import ModelForm

from shop_divisionapp.models import Clothes_assemble, Clothes_choice, Clothes_option_title, Clothes_option_size, \
    Clothes_option_detail_size


class Create_clothes_assemble_Form(ModelForm):
    class Meta:
        model = Clothes_assemble
        fields = ['clothes_title']


class Create_clothes_choice_Form(ModelForm):
    class Meta:
        model = Clothes_choice
        fields = ['clothes_choice_title', 'clothes_choice_size', 'clothes_choice_color',]


class Create_clothes_choice_title(ModelForm):
    class Meta:
        model = Clothes_option_title
        fields = ['clothes_title']

class Create_clothes_choice_option_size(ModelForm):
    class Meta:
        model = Clothes_option_size
        fields = ['clothes_option_parent', 'clothes_size']

class Create_clothes_choice_option_size_testing(ModelForm):
    class Meta:
        model = Clothes_option_detail_size
        fields = []
