# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, authorfname, authorlname):
        self.title = title
        self.price = price

        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapters = []

    def addchapter(self, name, pages):
        self.chapters.append((name, pages))


b1 = Book("War and Peace", 39.0, "Leo", "Tolstoy")

b1.addchapter("Chapter 1", 125)
b1.addchapter("Chapter 2", 97)
b1.addchapter("Chapter 3", 143)

print(b1.title)
