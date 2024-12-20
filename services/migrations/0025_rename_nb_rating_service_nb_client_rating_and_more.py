# Generated by Django 4.2.16 on 2024-11-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_service_nb_rating_alter_service_nb_request'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='nb_rating',
            new_name='nb_client_rating',
        ),
        migrations.AddField(
            model_name='service',
            name='nb_total_rating',
            field=models.IntegerField(default=0),
        ),
    ]
