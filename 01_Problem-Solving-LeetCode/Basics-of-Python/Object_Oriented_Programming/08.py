class Car:
    def __init__(self,speed,colour):
        self.speed = speed
        self.colour = colour
    
    def set_speed(self,value):
        self.speed = value
    
    def get_speed(self):
        return self.speed
    
    def set_colour(self,col):
        self.colour = col
    
    def get_colour(self):
        return self.colour


ford = Car(230,'red')
honda = Car(200,'black')
audi =Car(250,'blue')

# print(ford.speed)

ford.set_speed(240)
ford.set_colour('Green')

print(ford.get_speed())
print(ford.get_colour())





