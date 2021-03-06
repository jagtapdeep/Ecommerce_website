# Generated by Django 3.1 on 2020-09-29 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20200929_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(default=None, upload_to='uploads/products'),
        ),
    ]
