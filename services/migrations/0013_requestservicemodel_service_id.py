# Generated by Django 4.2.16 on 2024-11-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_alter_requestservicemodel_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestservicemodel',
            name='service_id',
            field=models.IntegerField(default=0),
        ),
    ]