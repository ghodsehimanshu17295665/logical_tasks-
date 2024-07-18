# Inheritance in Python :-

# 1. Single inheritance:-
print("1. Single Inheritance:-------")


# Base class
class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")


# Child class
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


# Create object of Car
car = Car()

# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()


# 2. Multiple Inheritance:-
print("2. Multiple Inheritance:-------")


# Parent class 1
class Person:
    def person_info(self, name, age):
        print("Inside Person class")
        print("Name:", name, "Age:", age)


# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print("Inside Company class")
        print("Name:", company_name, "location:", location)


# Child class
class Employee(Person, Company):
    def Employee_info(self, salary, skill):
        print("Inside Employee class")
        print("Salary:", salary, "Skill:", skill)


# Create object of Employee
emp = Employee()
# access data
emp.person_info("Jessa", 28)
emp.company_info("Google", "Delhi")
emp.Employee_info(12000, "Machine Learning")


# 3. Multilevel Inheritance
print("3. Multilevel Inheritance:---------")


# Base class
class Vehicle:
    def Vehicle_info(self):
        print("Inside Vehicle class")


# Child class
class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")


# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print("Inside SportsCar class")


# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()
