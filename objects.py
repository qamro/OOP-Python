class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def describe(self):
        print(f"This is a {self.color} {self.model} from {self.year}. For sale: {self.for_sale}")

    def drive(self):
        print(f"The {self.model} is now driving.")
        
    def stop(self):
        print(f"The {self.model} has stopped.")
        
        
                
# Create objects of the Car class

car1 = Car("Clio Classique", 2007, "Grey", False)       
car1.describe()
car1.drive()
car1.stop()

print(car1.model)  # Output: Clio Classique
print(car1.year)   # Output: 2007
print(car1.color)  # Output: Grey
print(car1.for_sale)  # Output: False

print()  # Print a blank line for separation

car2 = Car("BMW M3", 2026, "Red", True)
car2.describe()
car2.drive()
car2.stop()

print(car2.model)  # Output: BMW M3
print(car2.year)   # Output: 2026
print(car2.color)  # Output: Red
print(car2.for_sale)  # Output: True