from django.db import models

# Create your models here.
from accountapp.models import Self_user


class Self_box(models.Model):
    self_box = models.ForeignKey(Self_user, on_delete=models.CASCADE, related_name='self_box')

    box_name = models.CharField(max_length=15)