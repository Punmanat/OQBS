# Generated by Django 2.2 on 2019-05-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190429_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='barbershop',
            name='pic',
            field=models.ImageField(default='shop_pic/default.jpg', upload_to='shop_pic'),
        ),
    ]
