# Generated by Django 4.2.7 on 2023-12-18 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car/media/uploads/')),
                ('car_name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=8)),
                ('details', models.TextField()),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_brand.brand')),
            ],
        ),
    ]
