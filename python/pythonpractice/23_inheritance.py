# Create a base class Shape with a method area that returns 0.
# Then, create two subclasses Rectangle and Circle that override the area method to
# calculate the area of a rectangle and a circle, respectively.


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rec = Rectangle(10, 20)
print("area of Rectangle:- ", rec.area())

cir = Circle(3)
print("Area of Circle:- ", cir.area())
