# Generated by Django 4.2.7 on 2023-12-19 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='slug',
        ),
    ]