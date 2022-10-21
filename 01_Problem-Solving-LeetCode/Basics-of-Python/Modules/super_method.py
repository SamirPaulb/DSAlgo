class Parent:
    def __init__(self,name):
        print('Parent__init__',name)

class Parent2:
    def __init__(self,name):
        print('Parent2__init__',name)


class Child(Parent,Parent2):
    def __init__(self):
        print("Child__init__")
        Parent.__init__(self,'max')
        Parent2.__init__(self,'tom')
        


child= Child()
print(Child.__mro__)
