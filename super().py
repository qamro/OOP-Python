# super() is a function that returns a proxy object that delegates method calls to a parent or sibling class of type. 
# The super() function is commonly used in the context of multiple inheritance,
# where it can be used to call methods from a parent class without explicitly naming it.


class Shape:  # this class is the parent class and its called the super class
    def __init__(self, color):
        self.color = color
class circle(Shape):  # this class is the child class and its called the sub class
    def __init__(self, color, radius):
        super().__init__(color)  # here we are calling the __init__ method of the parent class Shape using the super() function
        self.radius = radius
class rectangle(Shape):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width  

class square(Shape):
    def __init__(self, color, width):
        super().__init__(color)
        self.width = width
