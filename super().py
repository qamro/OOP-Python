# super() is a function that returns a proxy object that delegates method calls to a parent or sibling class of type. 
# The super() function is commonly used in the context of multiple inheritance,
# where it can be used to call methods from a parent class without explicitly naming it.


class Shape:  # this class is the parent class and its called the super class
    def __init__(self, color):
        self.color = color
        
    def describe(self):
        print(f"This is a {self.color} shape")
        
            
class circle(Shape):  # this class is the child class and its called the sub class
    def __init__(self, color, radius):
        super().__init__(color)  # here we are calling the __init__ method of the parent class Shape using the super() function
        self.radius = radius
        
    def describe(self):
        print(f"the area of the circle is {3.14 * self.radius * self.radius}")
        super().describe()  # here we are calling the describe method of the parent class Shape using the super() function
        
        
class rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width  

    def describe(self):
            print(f"the area of the rectangle is {self.height * self.width}")
            super().describe()  # here we are calling the describe method of the parent class Shape using the super() function

class square(Shape):
    def __init__(self, color, width):
        super().__init__(color)
        self.width = width
    def describe(self):
        print(f"the area of the square is {self.width * self.width}")
        super().describe()  # here we are calling the describe method of the parent class Shape using the super() function

circle = circle("red", 5)
print(circle.color)
print(circle.radius)
circle.describe()

print()

rectangle = rectangle("blue", 4, 6)
print(rectangle.color)
print(rectangle.height)
print(rectangle.width)
rectangle.describe()

print()

square = square("green", 4)
print(square.color)
print(square.width)
square.describe()