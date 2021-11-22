from abc import ABC, abstractclassmethod
class Shape(ABC):
    @abstractclassmethod  # --->> this is called Decorator and identify to use this abstract class not all the fuction of the super class
    def area(self): pass

    @abstractclassmethod  # --->> this is called Decorator and identify to use this abstract class not all the fuction of the super class
    def perimeter(self): pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side
    def area(self):
        return self.__side*self.__side
    def perimeter(self):
        return 4*self.__side

square = Square(5)
print(square.area())
print(square.perimeter())

