# Generated by Django 4.2.16 on 2024-11-21 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='users_customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
