# Generated by Django 5.0.6 on 2024-05-11 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_remove_user_id_user_userid_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file_field',
            field=models.FileField(default=None, upload_to='files/'),
        ),
        migrations.AddField(
            model_name='user',
            name='float_field',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='user',
            name='image_field',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='user',
            name='text_field',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='time_field',
            field=models.TimeField(default=datetime.time(11, 49, 35, 621895)),
        ),
        migrations.AddField(
            model_name='user',
            name='url_field',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
