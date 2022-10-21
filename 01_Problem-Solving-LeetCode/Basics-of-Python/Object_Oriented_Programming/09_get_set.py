class Car:
    def __init__(self,speed,colour):
        self.__speed = speed
        self.__colour = colour

    def set_speed(self,speed):
        self.__speed = speed
    def get_speed(self):
        return self.__speed
    
    def set_colour(self,colour):
        self.__colour = colour
    def get_colour(self):
        return self.__colour
    
ford = Car(230,'red')
honda = Car(200,'black')
audi = Car(250,'blue')

ford.set_colour('green')
ford.set_speed(300)
ford = Car(230,'red')


print(ford.get_colour())
print(ford.get_speed())

