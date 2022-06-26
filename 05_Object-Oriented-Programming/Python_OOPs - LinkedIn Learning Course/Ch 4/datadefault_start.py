# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str
    author: str
    pages: int
    price: float
