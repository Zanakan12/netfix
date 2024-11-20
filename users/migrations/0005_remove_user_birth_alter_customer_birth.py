# Generated by Django 4.2.16 on 2024-11-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customer_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth',
        ),
        migrations.AlterField(
            model_name='customer',
            name='birth',
            field=models.DateField(default='2000-01-01', null=True),
        ),
    ]