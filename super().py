# super() is a function that returns a proxy object that delegates method calls to a parent or sibling class of type. 
# The super() function is commonly used in the context of multiple inheritance,
# where it can be used to call methods from a parent class without explicitly naming it.

class circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
class rectangle:
    pass

class square:
    pass