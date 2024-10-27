class Vehicle:
    def describe(self):
        print("A vehicle")

class Car(Vehicle):
    def describe(self):
        print("A car with 4 wheels")

class Bike(Vehicle):
    def describe(self):
        print("A bike with 2 wheels")

def describe_vehicle(vehicle):
    vehicle.describe()

describe_vehicle(Car())  
describe_vehicle(Bike()) 
