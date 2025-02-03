class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
def main():
    square = Square(4)
    print(f"The area of the square is {square.area()}")

    triangle = Triangle(3, 4)
    print(f"The area of the triangle is {triangle.area()}")
main()