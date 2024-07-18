#Create a base class Shape with a method draw. 
# Then, create two subclasses Circle and Square that override the draw method.

class Shape:
    def draw(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")


def draw_shape(shape):
    shape.draw()


circle = Circle()

square = Square()

draw_shape(circle)  # Outputs: Drawing a circle
draw_shape(square)  # Outputs: Drawing a square
