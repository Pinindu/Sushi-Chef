# Generated by Django 3.1.2 on 2020-12-11 10:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0021_auto_20201206_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.ForeignKey(on_delete=models.SET('Anonymous User'), related_name='customerreview_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
