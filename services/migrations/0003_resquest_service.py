# Generated by Django 4.2.16 on 2024-11-21 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_birth'),
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resquest_Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.company')),
            ],
        ),
    ]
