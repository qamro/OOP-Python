# abstract classes is classes that we cannot create an object of that class 
# but we can inherit from that class and create an object of the child class

# abstract classes contain abstract methods that we cant implement directly in the abstract class
# but we can implement them in the child class
# we require the child class to implement the abstract methods of the abstract class

# we need to import the ABC module to create an abstract class and abstract methods
# ABC stands for Abstract Base Class
# ABC module provides the infrastructure for defining abstract base classes in Python

from abc import ABC, abstractmethod

class Vehicle(ABC): # like that we can create an abstract class by inheriting from the ABC class
    
    @abstractmethod # like that we can create an abstract method by using the @abstractmethod decorator
    def start(self):
        pass # we can use the pass statement to indicate that the method is abstract and has no implementation
    def stop(self):
        pass
    
class Car(Vehicle): # here we are inheriting from the abstract class Vehicle
    
    def start(self): # here we are implementing the abstract method start
        print("Car is starting")
        
    def stop(self): # here we are implementing the abstract method stop
        print("Car is stopping")


car = Car() # here we are creating an object of the child class Car
car.start() # here we are calling the start method of the child class Car
car.stop() # here we are calling the stop method of the child class Car



"""
NOTE:
just a simple notes
-the abstract class can have both abstract and non-abstract methods
-the child class must implement all the abstract methods of the abstract class 
-if the child doesnt implement all the abstract methods, the child will be an abstract class too so we cant create object from it
"""
            