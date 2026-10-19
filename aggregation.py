# aggregation represents a relationship between two classes where one class (the whole) contains other classes (the parts).
# In aggregation, the lifetime of the part is not managed by the whole, meaning that the part can exist independently of the whole.
# unlike composition, where the whole is responsible for the lifetime of the parts

class library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Aggregation: library contains books

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Library: {self.name}")
        for book in self.books:
            print(f"- {book.title} by {book.author}")
            
class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Example usage
library = library("Sétif Library")                    
book1 = book("Fucking ESTIN", "Qamro")
book2 = book("How to get 5 in Archi", "Qamro")
book3 = book("How to study fucking electonic", "Qamro")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.display_books()