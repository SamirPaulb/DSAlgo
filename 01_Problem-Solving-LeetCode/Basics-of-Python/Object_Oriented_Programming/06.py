class car:
    def __init__(self,speed,color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color
        print("The __init__ is called")
        print("----------------------------------------------------------------")

ford = car(230,'red')
honda =car(200,'green')
audi = car(250,'blue')




