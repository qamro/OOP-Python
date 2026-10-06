# multilevel inheritance means that a class can inherit from another class which is already inherited from another class

class Animal:
        
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("HOOOW!!")
        
        
# here we are inheriting from both the animal and dog class       
class Kimi(Dog, Animal):  

    def speak_up(self):
        print("HOOOW!! HOOOW!!") 


kimi = Kimi("Kimi")
kimi.eat()
kimi.sleep()
kimi.speak()  
kimi.speak_up()  