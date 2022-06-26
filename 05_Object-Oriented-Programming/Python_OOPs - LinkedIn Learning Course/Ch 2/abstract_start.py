# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints


class GraphicShape:
    def __init__(self):
        super().__init__()

    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side


g = GraphicShape()

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())
