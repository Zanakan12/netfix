# Generated by Django 4.2.16 on 2024-11-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0019_alter_requestservicemodel_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestservicemodel',
            name='nb_request',
            field=models.IntegerField(default=0),
        ),
    ]