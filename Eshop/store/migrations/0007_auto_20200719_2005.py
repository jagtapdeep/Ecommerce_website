# Generated by Django 3.0.7 on 2020-07-19 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_userorder_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='order_id',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
