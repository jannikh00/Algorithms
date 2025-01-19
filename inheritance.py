# Assignment 1: Object-Oriented Programming

# Parent Class Vehicle
class Vehicle:
    # initializing Vehicle object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # function to display Vehicle object information
    def display_info(self):
        print(f"This is a {self.year} {self.make} {self.model}.")

# Car Child Class
class Car(Vehicle):
    # initializing Car object
    def __init__(self, make, model, year, number_of_doors, max_speed):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
        self.max_speed = max_speed

    # function to display Car object information
    def car_details(self):
        print(f"This {self.make} {self.model} has {self.number_of_doors} doors and a max speed of {self.max_speed} mph.")

# Truck Child Class
class Truck(Vehicle):
    # initializing Truck object
    def __init__(self, make, model, year, cargo_capacity, drive_type):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity
        self.drive_type = drive_type

    # function to display Truck object information
    def truck_info(self):
        print(f"This {self.make} {self.model} truck has a cargo capacity of {self.cargo_capacity} tons and {self.drive_type} drive.")

# Testing
# Objects
vehicle_1 = Vehicle("Toyota", "Supra", 2021)
car_1 = Car("Ford", "Mustang GT", 2024, 2, 180)
truck_1 = Truck("Ford", "F-150", 2023, 1.1, "4 wheel")

# Methods
vehicle_1.display_info()
car_1.display_info()
car_1.car_details()
truck_1.display_info()
truck_1.truck_info()