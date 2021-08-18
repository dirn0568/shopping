from django.db import models

# Create your models here.
from shop_divisionapp.models import Clothes_option_title


class Self_create_shop(models.Model):
    shop_title = models.CharField(max_length=15)

    shop_img = models.ImageField(upload_to='shop/', null=True)
    shop_name = models.CharField(max_length=15, unique=True)
    shop_cash = models.IntegerField(default=0)

    # shop_division = models.ForeignKey