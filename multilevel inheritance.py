# multilevel inheritance means that a class can inherit from another class which is already inherited from another class

class Animal:
        
    def __init__(self, name):
        self.name = name
        
                
    def eat(self):
        print(f"{self.name} is eating")    
        
    def sleep(self):
        print(f"{self.name} is asleep")

class Dog(Animal):
        
    def speak(self):
        print("HOOOW!!")
        
        
# here we are inheriting from the dog class which is already inherited from the animal class     
class Kimi(Dog):  

    def speak_up(self):
        print("HOOOW!! HOOOW!!") 


kimi = Kimi("Kimi")
kimi.eat()
kimi.sleep()
kimi.speak()  
kimi.speak_up()  