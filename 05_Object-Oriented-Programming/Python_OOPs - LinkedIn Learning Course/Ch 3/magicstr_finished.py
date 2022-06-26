# Python Object Oriented Programming by Joe Marini course example
# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # The __str__ function is used to return a user-friendly string
    # representation of the object
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # The __str__ function is used to return a developer-friendly string
    # representation of the object
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# print each object
print(b1)
print(b2)

# use str() and repr()
print(str(b1))
print(repr(b2))
