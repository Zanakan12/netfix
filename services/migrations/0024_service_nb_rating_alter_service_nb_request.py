# Generated by Django 4.2.16 on 2024-11-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_alter_service_field_alter_service_nb_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='nb_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='service',
            name='nb_request',
            field=models.IntegerField(default=0),
        ),
    ]
