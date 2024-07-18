# Inheritance :-

# 4. Hierarchical Inheritance:-
print("4.Hierarchical inheritance:------")


class Vehicle:
    def info(self):
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info("BMW")

obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")


# 5. Hybrid Inheritance:-
print("5.Hybrid Inheritance:---------------")


class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")


class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")


# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sport_car_info(self):
        print("Inside SportCar Class")


# Create Object:-
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sport_car_info()
