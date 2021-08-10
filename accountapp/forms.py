from django.forms import ModelForm

from accountapp.models import Self_user


class Self_userCreateForm(ModelForm):
    class Meta:
        model = Self_user
        fields = ['self_name', 'self_password', 'self_nickname']

class Self_userUpdateForm(ModelForm):
    class Meta:
        model = Self_user
        fields = ['self_name', 'self_nickname']