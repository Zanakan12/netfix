# Generated by Django 4.2.16 on 2024-11-23 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_alter_service_field_alter_service_nb_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='field',
            field=models.CharField(choices=[('all-in-one', 'All in One'), ('air-conditioner', 'Air Conditioner'), ('carpentry', 'Carpentry'), ('electricity', 'Electricity'), ('gardening', 'Gardening'), ('home-machines', 'Home Machines'), ('house-keeping', 'House Keeping'), ('interior-design', 'Interior Design'), ('locks', 'Locks'), ('painting', 'Painting'), ('plumbing', 'Plumbing'), ('water-heaters', 'Water Heaters')], max_length=30),
        ),
        migrations.AlterField(
            model_name='service',
            name='nb_request',
            field=models.IntegerField(default=2),
        ),
    ]