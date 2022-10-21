from Polygon import Polygon
from shape import Shape
class Triangle(Polygon,Shape):
    def area(self):
        return (self.get_width()*self.get_height())/2

