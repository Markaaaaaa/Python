class Library:
    library_name = "Central Library"

    def __init__(self, book_title):
        self.book_title = book_title

lib1 = Library("Python Programming")
lib2 = Library("Data Science")

print(lib1.library_name)
print(lib2.library_name)
print(lib1.book_title)
print(lib2.book_title)
