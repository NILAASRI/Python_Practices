#You are tasked with modeling a simple vehicle hierarchy in Python. 
#Your goal is to create a base class called Vehicle and a derived class called Car.

# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("Starting the", self.make, self.model)

    def stop(self):
        print("Stopping the", self.make, self.model)

# Derived class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, numberOfDoors):
        super().__init__(make, model)
        self.numberOfDoors = numberOfDoors

    def honk(self):
        print("Honking the horn of the", self.make, self.model)


# Create an instance of the Vehicle class
generic_vehicle = Vehicle("Generic", "Vehicle")
generic_vehicle.start()
generic_vehicle.stop()

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 4)
my_car.start()
my_car.honk()
my_car.stop()
'''
Output
Starting the Generic Vehicle
Stopping the Generic Vehicle
Starting the Toyota Camry
Honking the horn of the Toyota Camry
Stopping the Toyota Camry
'''