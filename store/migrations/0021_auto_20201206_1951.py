# Generated by Django 3.1.2 on 2020-12-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20201106_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(default='images/user/default.jpg', upload_to='images/user'),
        ),
    ]
