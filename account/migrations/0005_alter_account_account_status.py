# Generated by Django 3.2.7 on 2023-01-14 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_kyc_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_status',
            field=models.CharField(choices=[('active', 'Active'), ('pending', 'Pending'), ('in-active', 'In-active')], default='in-active', max_length=100),
        ),
    ]
