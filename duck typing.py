# duck typing means that if an object behaves like a certain type, it can be used as that type, regardless of its actual class.
# by using the same method name in different classes, we can achieve polymorphism in python

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
        
class Cat(Animal):
    def speak(self):
        print("Meow!")
        
class Car:
    def speak(self):
        print("Vroom!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()  # This will call the speak method of each object, regardless of its class                            