class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def area(self):
        return 0.5 * self.b * self.h

c1 = Circle(7)
r1 = Rectangle(20, 12)
t1 = Triangle(5, 15)

print(f"Area of circle: {c1.area()}")
print(f"Area of rectangle: {r1.area()}")
print(f"Area of triangle: {t1.area()}")

