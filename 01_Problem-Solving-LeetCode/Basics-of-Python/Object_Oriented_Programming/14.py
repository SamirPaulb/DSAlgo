import math
class Calculator:
    def __init__(self,number):
        self.number = number
    def get_values(self):
        print(f"For the number {self.number}; \n Square is: {self.number*self.number} \n Cube is: {self.number*self.number*self.number} \n Squareroot is: {math.sqrt(self.number)}")

num = Calculator(16)
num.get_values()



