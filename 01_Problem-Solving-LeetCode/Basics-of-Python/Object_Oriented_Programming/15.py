class Calculator:
    def __init__(self,number):
        self.number = number
    
    def square(self):
        print(f"square is {self.number**2}")
    def cube(self):
        print(f"cube is {self.number**3}")
    def squareroot(self):
        print(f"Squareroot is {self.number**0.5}")

num = Calculator(9)
num.square()
num.cube()
num.squareroot()
