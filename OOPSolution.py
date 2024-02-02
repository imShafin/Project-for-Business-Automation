class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity
    def ShowCarInfo(self):
        print("Car Information:", end="\n\t")
        print(self.year, self.name, self.model, end="\n\t")
        print("Battery Capacity:", self.battery_capacity)

class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency
    def ShowCarInfo(self):
        print("Car Information:", end="\n\t")
        print(self.year, self.name, self.model, end="\n\t")
        print("Fuel Efficiency:", self.fuel_efficiency)

if __name__ == "__main__":
    CarType = input("Enter car type (Electric/Gas): ")
    if CarType == "Electric":
        Name = input("Enter Name: ")
        Model = input("Enter model: ")
        Year = input("Enter year: ")
        Battery = input("Enter battery capacity (kWh): ") 
        car = ElectricCar(Name, Model, Year, Battery)
        car.ShowCarInfo()
    else:
        Name = input("Enter Name: ")
        Model = input("Enter model: ")
        Year = input("Enter year: ")
        Battery = input("Enter fuel effeciency(MPG): ") 
        car = ElectricCar(Name, Model, Year, Battery)
        car.ShowCarInfo()
