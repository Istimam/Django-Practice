# Generated by Django 5.0.6 on 2024-06-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_userbankaccount_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_bankrupt', models.BooleanField(default=False)),
            ],
        ),
    ]
