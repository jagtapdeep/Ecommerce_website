# Generated by Django 3.0.7 on 2020-07-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(default='guest', max_length=50),
        ),
    ]
