# multiple inheritance means that a class can inherit from multiple classes

class Animal:
        
    def __init__(self, name):
        self.name = name
        
                
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog:
        
    def speak(self):
        print("HOOOW!!")
        
        
# here we are inheriting from both the animal and dog class       
class Kimi(Animal, Dog):  

    def speak_up(self):
        print("HOOOW!! HOOOW!!") 


kimi = Kimi("Kimi")
kimi.eat()
kimi.sleep()
kimi.speak()  
kimi.speak_up()  


"""
NOTE:
just a simple note
if all the parents have __init__ method 
then the child class will only inherit the _init__ method of the first parent class and not the other parents   
"""