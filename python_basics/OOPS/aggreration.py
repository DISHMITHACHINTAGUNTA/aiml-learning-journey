#aggregation: it represents a relationship where one object contains references to one more INDEPENDENT  objects

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self,title, author):
        self.title=title
        self.author=author

library=Library("Alluri Public Library")

b1=Book("The Palace of Illusions","Chitra Banerjee Divakaruni")
b2=Book("The Pregnant King","Devdutt Pattanaik")

library.add_book(b1)
library.add_book(b2)

print(library.name)
print(library.list_books())
for i in library.list_books():
    print(i)



