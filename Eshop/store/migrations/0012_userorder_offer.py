# Generated by Django 3.0.7 on 2020-07-22 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='offer',
            field=models.IntegerField(default=0),
        ),
    ]
