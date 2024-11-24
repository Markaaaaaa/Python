class Libray:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} Author {self.author}, ISBN: {self.isbn}, Status: {status}"
class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name
        self.borrowed_books = []
class set:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, title, author, isbn):
        self.books.append(Libray(title, author, isbn))
        print(f"Book '{title}' added.")

    def add_borrower(self, borrower_id, name):
        self.borrowers.append(Borrower(borrower_id, name))
        print(f"Borrower '{name}' added.")

    def borrow_book(self, borrower_id, isbn):
        borrower = self.find_borrower(borrower_id)
        book = self.find_book(isbn)
        if borrower and book and book.available:
            book.available = False
            borrower.borrowed_books.append(book)
            print(f"'{book.title}' borrowed by {borrower.name}.")
        else:
            print("Borrowing failed.")

    def return_book(self, borrower_id, isbn):
        borrower = self.find_borrower(borrower_id)
        if borrower:
            for book in borrower.borrowed_books:
                if book.isbn == isbn:
                    book.available = True
                    borrower.borrowed_books.remove(book)
                    print(f"'{book.title}' returned by {borrower.name}.")
                    return
        print("Return failed.")

    def display_books(self):
        for book in self.books:
            print(book)

    # Find a book by ISBN
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def find_borrower(self, borrower_id):
        for borrower in self.borrowers:
            if borrower.borrower_id == borrower_id:
                return borrower
        return None

library = set()
library.add_book("One Hundred Yeas of Solitude", "García Márquez", "9781574397112")
library.add_book("Hamlet", "Shakespeare", "9781586638443")
library.add_borrower(17, "Mark")
library.borrow_book(17, "9781586638443")
library.display_books()
library.return_book(17, "9781586638443")
library.display_books()
