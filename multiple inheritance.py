# multiple inheritance means that a class can inherit from multiple classes

class Animal:
        
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def speak(self):
        print("HOOOW!!")
        
class Kimi(Dog, Animal):  # here we are inheriting from both the animal and dog class

    def speak_up(self):
        print("HOOOW!! HOOOW!!") 


kimi = Kimi("Kimi")
kimi.eat()
kimi.sleep()
kimi.speak()  
kimi.speak_up()  