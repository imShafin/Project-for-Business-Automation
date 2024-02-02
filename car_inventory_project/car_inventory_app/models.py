from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()

class ElectricCar(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    battery_capacity = models.FloatField()

class GasCar(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    fuel_capacity = models.FloatField()
