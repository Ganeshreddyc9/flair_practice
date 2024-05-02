from abc import ABC,abstractproperty

class Shape(ABC):
    @abstractproperty

    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius *self.radius

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

rectangle = Rectangle(3,4)
print(rectangle.area)

circle = Circle(12)
print(circle.area)
