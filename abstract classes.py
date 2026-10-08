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
    
    