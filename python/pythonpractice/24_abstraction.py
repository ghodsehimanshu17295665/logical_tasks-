# Create an abstract class Shape with an abstract method area.
# Then, create two subclasses Circle and Rectangle that implement the area method.

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5)
print(f"Circle area: {circle.area()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
