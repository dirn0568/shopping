from django.db import models

# Create your models here.

class Clothes_assemble(models.Model):
    clothes_title = models.CharField(max_length=30)

class Clothes_choice(models.Model):
    clothes_choice_title = models.ForeignKey(Clothes_assemble, on_delete=models.CASCADE, related_name='clothes_choice_title')

    clothes_choice_size = models.CharField(max_length=30)
    clothes_choice_color = models.CharField(max_length=30)





class Clothes_option_title(models.Model):
    clothes_title = models.CharField(max_length=30)

class Clothes_option_size(models.Model):
    clothes_option_parent = models.ForeignKey(Clothes_option_title, on_delete=models.CASCADE, related_name='clothes_option_parent')

    clothes_size = models.CharField(max_length=30)

class Clothes_option_detail_size(models.Model):
    clothes_option_detail = models.ForeignKey(Clothes_option_size, on_delete=models.CASCADE, related_name='clothes_option_detail')




# class test333(models.Model):



