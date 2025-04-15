import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'

class Square(Shape):

    def __init__(self,side):
        self.side= side

    def area(self):
        return self.side ** 2


class Circle(Shape):

    def __init__(self,radius):
        self.radius= radius

    def area(self):
       return math.pi * (self.radius ** 2)

class Cube(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * self.side ** 2

class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

square = Square(5)
circle = Circle(3)
cube = Cube(4)
cylinder = Cylinder(4,3)

print(square)
print(square.area())

print(circle)
print(circle.area())

print(cube)
print(cube.area())

print(cylinder)
print(cylinder.area())
