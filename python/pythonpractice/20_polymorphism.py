# Polymorphism in Python

# Method overriding :-


class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print("Details:", self.name, self.color, self.price)

    def max_speed(self):
        print("Vehicle max speed is 150")

    def change_gear(self):
        print("Vehicle change 6 gear")


# inherit from vehicle class
class Car(Vehicle):

    def max_speed(self):
        print("Car max speed is 240")

    def change_gear(self):
        print("Car change 7 gear")


# Car object:-
car = Car("car X1", "Red", 400000)
car.show()
# Calls Methods from car class:-
car.max_speed()
car.change_gear()

# Vehicle Object:-
vehicle = Vehicle("Truck Y1", "White", 750000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear()
