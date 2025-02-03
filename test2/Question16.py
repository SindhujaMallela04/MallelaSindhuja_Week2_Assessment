import math
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        print(f"The area of Rectangle is : {self.length * self.breadth}")
    
class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        print(f"The area of the circle is {math.pi * self.radius * self.radius}")
    
def main():
    rectangle = Rectangle(3, 4)
    rectangle.calculate_area()
    circle = Circle(5)
    circle.calculate_area()
main()
    