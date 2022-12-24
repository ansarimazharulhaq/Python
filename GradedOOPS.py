class Shape:
    
    def __init__(self, name):
        self.name = name
        print("Calculating the area of",self.name,"....")

    def area(self):
        pass

class Circle(Shape):

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def area(self):
        self.pi = 3.142
        return self.pi * self.radius**2

class Square(Shape):

    def __init__(self, name, side):
        self.name = name
        self.side = side

    def area(self):
        return self.side**2
 
areaOfCircle = Circle(Shape("Circle"), 2)
print("Area of circle is ",areaOfCircle.area())

areaOfSquare = Square(Shape("Square"), 5)
print("Area of square is ",areaOfSquare.area())