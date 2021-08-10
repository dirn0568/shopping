from django.forms import ModelForm, forms, CharField

from accountapp.models import Self_user, Self_data


class Self_userCreateForm(ModelForm):
    class Meta:
        model = Self_user
        fields = ['self_name', 'self_password', 'self_nickname']

class Self_userUpdateForm(ModelForm):
    class Meta:
        model = Self_user
        fields = ['self_name', 'self_nickname']

class Self_userLoginForm(ModelForm):
    class Meta:
        model = Self_data
        fields = ['self_name', 'self_password']