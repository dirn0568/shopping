from django.db import models

# Create your models here.


# 주문 사항 양식
class Clothes_option_title(models.Model):
    clothes_title = models.CharField(max_length=30)
class Clothes_option_detail_title(models.Model):
    clothes_option_detail_title = models.ForeignKey(Clothes_option_title, on_delete=models.CASCADE, related_name='clothes_option_detail_title')
class Clothes_option_size(models.Model):
    clothes_option_size = models.ForeignKey(Clothes_option_title, on_delete=models.CASCADE, related_name='clothes_option_size')
    clothes_size = models.CharField(max_length=30)
class Clothes_option_color(models.Model):
    clothes_option_color = models.ForeignKey(Clothes_option_title, on_delete=models.CASCADE, related_name='clothes_option_color')
    clothes_color = models.CharField(max_length=30)

# 세부 주문 조건
class Clothes_option_detail_size(models.Model):
    clothes_option_detail_size = models.ForeignKey(Clothes_option_size, on_delete=models.CASCADE, related_name='clothes_option_detail_size')
class Clothes_option_detail_color(models.Model):
    clothes_option_detail_color = models.ForeignKey(Clothes_option_color, on_delete=models.CASCADE, related_name='clothes_option_detail_color')
class Clothes_option_number(models.Model):
    order_number = models.IntegerField(default=1)

# class Clothes_option_detail_color(models.Model):
#     clothes_option_detail = models.ForeignKey(Clothes_option_size, on_delete=models.CASCADE, related_name='clothes_option_detail')




# class test333(models.Model):



