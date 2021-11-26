class Polygon:
    __height = None
    __width = None
    def set_values(self,height,width):
        self.__height = height
        self.__width = width
    def get_height(self):
        return self.__height
    def get_width(self):
        return self.__width

class Rectangle(Polygon):
    def area(self): 
        return self.get_height()*self.get_width()

class Triangle(Polygon):
    def area(self):
        return (self.get_width()*self.get_height())/2

rect = Rectangle()
tri = Triangle()

rect.set_values(50,40)
tri.set_values(50,40)


print(rect.area())
print(tri.area())