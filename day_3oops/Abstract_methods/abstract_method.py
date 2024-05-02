from abc import ABC,abstractmethod


"""
abstractmethod:

This decorator is used to declare abstract methods within an abstract class.
Subclasses must provide concrete implementations for these methods"""


# an absract class is considered as a skeliton of other class


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius =radius

    def area(self):
        return 3.14 * self.radius *self.radius

circle = Circle(5)
print(circle.area())

