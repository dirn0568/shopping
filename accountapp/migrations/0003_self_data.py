# Generated by Django 3.2.2 on 2021-08-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_auto_20210808_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Self_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_name', models.CharField(max_length=15)),
                ('self_password', models.CharField(max_length=15)),
                ('self_pk', models.IntegerField(default=0)),
            ],
        ),
    ]
