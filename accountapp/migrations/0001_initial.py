# Generated by Django 3.2.2 on 2021-08-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Self_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_name', models.CharField(max_length=15, unique=True, verbose_name='아이디')),
                ('self_password', models.CharField(max_length=15, verbose_name='비밀번호')),
                ('self_nickname', models.CharField(max_length=15, unique=True, verbose_name='닉네임')),
            ],
        ),
        migrations.CreateModel(
            name='Self_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('self_name', models.CharField(max_length=15)),
                ('self_password', models.CharField(max_length=15)),
                ('self_pk', models.IntegerField(default=0)),
                ('self_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='self_data', to='accountapp.self_user')),
            ],
        ),
    ]
