# inheritance allows a class to inherit attributes and methods from another class 
# it helps with code reusability

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")            

# all these methods and the constructor of the animal class will be inherited to any class we want

class Dog(Animal):
    def speak(self):  # here we define a specific method for a dog class
        print("HOOOW!!")


class Cat(Animal):
    def speak(self):  # here we define a specific method for a cat class
        print("MEOWW!!")                


dog = Dog("Jack")
dog.eat()
dog.sleep()
dog.speak()

print()

cat = Cat("Rosa")
cat.eat()
cat.sleep()
cat.speak()