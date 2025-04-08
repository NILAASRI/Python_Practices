class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def area(self):
        print(self.length * self.breadth)

    def perimeter(self):
        print(2 * (self.length + self.breadth))

r = Rectangle()

r.length = int(input())
r.breadth = int(input())

r.area()
r.perimeter()
