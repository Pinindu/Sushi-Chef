# Generated by Django 3.0.6 on 2020-10-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_chefreview_customer_order_orderedproducts_payment_productimages_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='place',
            field=models.CharField(choices=[('Main Product Image', 'Main Product Image'), ('Sub Image 1', 'Sub Image 1'), ('Sub Image 2', 'Sub Image 2')], max_length=20),
        ),
    ]