# car_inventory_app/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Car, ElectricCar, GasCar

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        car_type = data['carType']

        car = Car.objects.create(
            name=data['name'],
            model=data['model'],
            year=data['year'],
        )

        if car_type == 'ElectricCar':
            ElectricCar.objects.create(
                car=car,
                battery_capacity=data['batteryCapacity']
            )
        elif car_type == 'GasCar':
            GasCar.objects.create(
                car=car,
                fuel_capacity=data['fuelCapacity']
            )

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_cars(request):
    cars = Car.objects.all()
    car_data = []

    for car in cars:
        if hasattr(car, 'electriccar'):
            car_type = 'ElectricCar'
            capacity = 'batteryCapacity' + ' kWh'
        elif hasattr(car, 'gascar'):
            car_type = 'GasCar'
            capacity = 'fuelCapacity' + ' MPG'
        else:
            car_type = 'Car'

        car_data.append({
            'name': car.name,
            'model': car.model,
            'year': car.year,
            'car_type': car_type, 
            'capacity': capacity,
        })

    return JsonResponse(car_data, safe=False)
