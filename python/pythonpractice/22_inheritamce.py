# Create a parent class Vehicle with attributes make and model, and a method display_info.
# Then, create a child class Car that inherits from Vehicle and adds an attribute number_of_doors and a method display_car_info.


class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Vehicle):

    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def display_car_info(self):
        return (
            f"{self.display_info()}, Number of doors: {self.number_of_doors}"
        )


car = Car("Toyota", "Corolla", 4)
print(car.display_car_info())
