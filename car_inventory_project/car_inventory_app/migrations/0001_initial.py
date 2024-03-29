# Generated by Django 5.0.1 on 2024-01-31 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ElectricCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_capacity', models.FloatField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_inventory_app.car')),
            ],
        ),
        migrations.CreateModel(
            name='GasCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_capacity', models.FloatField()),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='car_inventory_app.car')),
            ],
        ),
    ]
