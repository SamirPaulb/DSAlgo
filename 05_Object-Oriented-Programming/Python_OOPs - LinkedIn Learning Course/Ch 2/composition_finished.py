# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        # Use references to other objects, like author and chapters
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.95, auth)

b1.addchapter(Chapter("Chapter 1", 104))
b1.addchapter(Chapter("Chapter 2", 89))
b1.addchapter(Chapter("Chapter 3", 124))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())
