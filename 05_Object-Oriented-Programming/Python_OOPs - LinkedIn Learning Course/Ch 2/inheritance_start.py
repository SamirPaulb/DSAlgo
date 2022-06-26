# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
