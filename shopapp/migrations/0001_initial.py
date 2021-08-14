# Generated by Django 3.2.2 on 2021-08-14 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Self_box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_img', models.ImageField(upload_to='shop/')),
                ('box_name', models.CharField(max_length=15)),
                ('box_cash', models.IntegerField(default=0)),
                ('self_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='self_box', to='accountapp.self_user')),
            ],
        ),
    ]
