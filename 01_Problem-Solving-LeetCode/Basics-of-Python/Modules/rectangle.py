from Polygon import Polygon
from shape import Shape

class Rectangle(Polygon,Shape):
    def area(self): 
        return self.get_height()*self.get_width()