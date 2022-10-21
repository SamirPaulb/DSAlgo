#from Inheritance import Rectangle(Polygon)
#from Inheritance import Triangle(Polygon)
from Polygon import Polygon
from rectangle import Rectangle
from triangle import Triangle
from shape import Shape



rect = Rectangle()
tri = Triangle()

rect.set_colour('red')
tri.set_colour('blue')


rect.set_values(50,40)
tri.set_values(50,40)


print(rect.area())
print(tri.area())

print(rect.get_colour())
print(tri.get_colour())

