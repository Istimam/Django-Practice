# Generated by Django 5.0.6 on 2024-06-03 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='album',
            name='release_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
