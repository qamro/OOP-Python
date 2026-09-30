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


class Dog(Animal):
    def speak(self):
        print("HOOOW!!")


class Cat(Animal):
    def speak(self):
        print("MEOWW!!")                


        