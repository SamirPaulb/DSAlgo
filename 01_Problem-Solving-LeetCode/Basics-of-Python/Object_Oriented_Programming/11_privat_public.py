class Hello:
    def __init__(self,name):
        self.a = 10
        self._b = 20
        self.__c = 30
    def public_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print('public')
    
 hello = Hello('Name')
 print(hello.a)
 print(hello._b)
 hello.public_method()
 
