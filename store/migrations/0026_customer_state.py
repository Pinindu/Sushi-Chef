# Generated by Django 3.1.2 on 2020-12-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_auto_20201214_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
