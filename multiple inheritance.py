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
        
        
# here we are inheriting from both the animal and dog class(we put the child class(Dog) first then the parent class(Animal)        
class Kimi(Dog, Animal):  

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
if u inherit from multiple classes and all these classes are parents so u can put the parent classes in any order 
but if u inherit from multiple classes and one of these classes is a child class so u have to put the child class first and then the parent class
"""