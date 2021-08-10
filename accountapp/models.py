from django.db import models

# Create your models here.
from django.db.models import CharField
from django.forms import IntegerField


class Self_user(models.Model):
    self_name = CharField(max_length=15, unique= True, null=False, verbose_name='아이디')
    self_password = CharField(max_length=15, null=False, verbose_name='비밀번호')
    self_nickname = CharField(max_length=15, unique= True, null=False, verbose_name='닉네임')

    models.DateTimeField(auto_now_add=True, verbose_name='생성시간')


class Self_data(models.Model):
    self_name = CharField(max_length=15, null=False)
    self_password = CharField(max_length=15, null=False)

    self_pk = models.IntegerField(default=0)






