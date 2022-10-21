class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        print(height)
        print(width)
        print("--------------------------------")

rect1 = Rectangle(30,20)
rect2 = Rectangle(50,10)


print(f'Area of rect1 is: {rect1.height*rect1.width}')
print(f'Area of rect2 is: {rect2.height*rect2.width}')



