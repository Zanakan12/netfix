# Generated by Django 4.2.16 on 2024-11-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0020_requestservicemodel_nb_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestservicemodel',
            name='nb_request',
        ),
        migrations.AddField(
            model_name='service',
            name='nb_request',
            field=models.IntegerField(default=0),
        ),
    ]
