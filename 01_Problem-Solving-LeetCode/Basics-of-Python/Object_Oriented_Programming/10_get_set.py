class Rectangle:
    def __init__(self,height,width):
        self.__height = height
        self.__width = width

    def set_height(self,height):
        self.__height = height
    def get_height(self):
        return self.__height

    def set_width(self,width):
        self.__width = width
    def get_width(self):
        return self.__width

    def area(self):
        return self.__height* self.__width

rect1 = Rectangle(30,40)
rect2 = Rectangle(50,10)

rect1.set_height(40)
rect1.set_width(50)
rect1 = Rectangle(30,40)

print(rect1.area())

    
