# Generated by Django 3.2.2 on 2021-08-18 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes_option_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_size', models.CharField(max_length=30)),
                ('clothes_option_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_option_size', to='shop_divisionapp.clothes_option_title')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_order_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_order_img', models.ImageField(null=True, upload_to='order/')),
                ('clothes_option_order_size', models.CharField(max_length=15)),
                ('clothes_option_order_color', models.CharField(max_length=15)),
                ('clothes_order_number', models.IntegerField(default=1)),
                ('clothes_order_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_order_pk', to='accountapp.self_user')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_detail_title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_option_detail_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_option_detail_title', to='shop_divisionapp.clothes_option_title')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_detail_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_option_detail_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_option_detail_size', to='shop_divisionapp.clothes_option_size')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes_option_detail_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothes_option_detail_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_option_detail_color', to='shop_divisionapp.clothes_option_color')),
            ],
        ),
        migrations.AddField(
            model_name='clothes_option_color',
            name='clothes_option_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothes_option_color', to='shop_divisionapp.clothes_option_title'),
        ),
    ]
