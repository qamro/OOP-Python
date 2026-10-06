# multiple inheritance means that a class can inherit from multiple classes

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("HOOOW!!")