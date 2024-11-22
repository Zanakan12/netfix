# Generated by Django 4.2.16 on 2024-11-21 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customer_user'),
        ('services', '0004_alter_resquest_service_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='resquest_service',
            name='intervall',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resquest_service',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer'),
        ),
    ]