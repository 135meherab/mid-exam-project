# Generated by Django 4.2.7 on 2023-12-19 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_remove_car_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='in_stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
