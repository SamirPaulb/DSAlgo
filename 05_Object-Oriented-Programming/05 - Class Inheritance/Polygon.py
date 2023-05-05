class Polygon:
    __height = None   # Private class atributes
    __width = None    # Private class atributes
    def set_values(self,height,width):
        self.__height = height  # setting values of private attrbutes by user input
        self.__width = width
    def get_height(self): # as we can not access these private attributes outside the class, so making this get_height() function to get the value of height
        return self.__height
    def get_width(self):  # as we can not access these private attributes outside the class, so making this get_width() function to get the value of width
        return self.__width

class Rectangle(Polygon):  # Rectangle class is inheriting the properties of the Polygon class
    def area(self): 
        return self.get_height()*self.get_width()

class Triangle(Polygon):   # Triangle class is inheriting the properties of the Polygon class
    def area(self):
        return (self.get_width()*self.get_height())/2

rect = Rectangle()
tri = Triangle()

rect.set_values(50,40)  # as Rectangle class inherited the methods of polygon class so we can directly use them in rectangle class
tri.set_values(50,40)   # as Triangle class  inherited the methods if Polygon class so we can directly use them in triangle class


print(rect.area())
print(tri.area())
