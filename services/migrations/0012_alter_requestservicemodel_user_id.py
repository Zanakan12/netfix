# Generated by Django 4.2.16 on 2024-11-22 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_customer_id_alter_customer_user'),
        ('services', '0011_requestservicemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestservicemodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]
