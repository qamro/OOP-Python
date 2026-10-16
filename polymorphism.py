# polymorphism is the ability of a function or method to work in different ways depending on the object it is acting upon.
# we can achieve polymorphism in python by using abstract classes and abstract methods
# we can achieve polymorphism also by using inheritance and duck typing

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

# create an object which is a list of shapes
shapes = [circle(5), rectangle(4, 6)]

# iterate through the list of shapes and call the area method on each shape
for shape in shapes:
    print(shape.area())