# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title):
        self.title = title


# TODO: access the class attribute


# TODO: Create some book instances
b1 = Book("Title 1")
b2 = Book("Title 2")

# TODO: Use the static method to access a singleton object
