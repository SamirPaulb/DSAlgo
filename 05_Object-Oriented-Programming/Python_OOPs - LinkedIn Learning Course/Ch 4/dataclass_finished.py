# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # You can define methods in a dataclass like any other
    def bookinfo(self):
        return f"{self.title}, by {self.author}"


# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses provide a default
# implementation of the __repr__ function
print(b1)

# comparing two dataclasses
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b1 == b3)

# change some fields, call a regular class method
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())
