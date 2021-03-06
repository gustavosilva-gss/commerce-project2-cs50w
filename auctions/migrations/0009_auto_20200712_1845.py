# Generated by Django 3.0.8 on 2020-07-12 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200711_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, validators=[django.core.validators.MaxLengthValidator(1000)]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MaxLengthValidator(1000)]),
        ),
    ]
