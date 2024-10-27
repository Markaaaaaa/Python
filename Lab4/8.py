class Book:
    def read(self):
        print("Reading a book")

class Novel(Book):
    def read(self):
        print("Enjoying a story")

class Textbook(Book):
    def read(self):
        print("Studying concepts")

books = [Novel(), Textbook()]
for book in books:
    book.read()
