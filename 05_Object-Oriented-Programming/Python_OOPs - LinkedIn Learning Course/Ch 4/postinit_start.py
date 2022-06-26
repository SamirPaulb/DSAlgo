# Python Object Oriented Programming by Joe Marini course example
# Using the postinit function in data classes

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # TODO: the __post_init__ function lets us customize additional properties
    # after the object has been initialized via built-in __init__


# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: use the description attribute
