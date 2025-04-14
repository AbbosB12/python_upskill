from abc import ABC, abstractmethod

from day04.abstractions import circle


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
        print("Calculating the square area")


class Circle(Shape):
    pass
class Cube(Shape):
    pass
class Cylinder(Shape):
    pass

square = Square(5)
# shape = Shape()
# circle = Circle()
# cube = Cube()
# cylinder = Cylinder()

print(square)
# print(circle)
# print(cube)
# print(cylinder)
# print(shape)
