# Generated by Django 3.0.7 on 2020-07-22 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20200721_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=15),
        ),
    ]
