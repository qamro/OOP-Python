# magic methods are special methods in python that have double underscores at the beginning and end of their names.
# they are also known as dunder methods (double underscore methods) like __init__, __str__, __len__, __eq__, __gt__, __lt__ ...
# they are automatically called by many of the built-in functions and operators in python.
# magic methods are used to define and customize the behavior of objects in python.

class Book:
    def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages
        
    # here we are overriding the __str__ magic method to customize the string representation of the Book object when we print it.
    # previously, when we print the object of the class Book, it will print the memory address of the object
    # but now it will print the string representation of the object as we defined in the __str__ method.    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    # the __eq__ magic method is used to compare two objects of the same class for equality.
    # it is called when we use the == operator to compare two objects of the same class.
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages
    
    # the __gt__ magic method is used to compare two objects of the same class for greater than.
    # it is called when we use the > operator to compare two objects of the same class
    def __gt__(self, other):
        return self.pages > other.pages
    
    # the __lt__ magic method is used to compare two objects of the same class for less than.
    # it is called when we use the < operator to compare two objects of the same class
    def __lt__(self, other):
        return self.pages < other.pages
    
    # the __add__ magic method is used to add two objects of the same class.
    # it is called when we use the + operator to add two objects of the same class
    def __add__(self, other):
        return f"{self.pages} + {other.pages}"
    
    # the __contains__ magic method is used to check if an object is contained in another object.
    # it is called when we use the in operator to check if an object is contained in another object
    def __contains__(self, item):
        return item in self.title or item in self.author 
    
    # the __getitem__ magic method is used to get the value of an attribute of an object.
    # it is called when we use the [] operator to get the value of an attribute of an object
    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "pages":
            return self.pages
        else:
            return "Invalid attribute"
        
    # the __len__ magic method is used to get the length of an object.
    # it is called when we use the len() function to get the length of an object
    def __len__(self):
        return self.pages
    
    
book1 = Book("Fucking ESTIN", "Qamro", 100)
book2 = Book("How to get 5 in Archi", "Qamro", 200)
book3 = Book("How to study fucking electonic", "Qamro", 300)

print(book1)  # Output: Title: Fucking ESTIN, Author: Qamro, Pages: 100
print(book1 == book2)  # Output: False
print(book1 > book2)  # Output: False
print(book1 < book2)  # Output: True
print(book1 + book2)  # Output: 100 + 200
print("ESTIN" in book1)  # Output: True
print(book1["title"])  # Output: Fucking ESTIN
print(book1["author"])  # Output: Qamro
print(book1["pages"])  # Output: 100
print(len(book1))  # Output: 100