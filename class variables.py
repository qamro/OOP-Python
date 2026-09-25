class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = Car("Clio Classique", 2007, "Grey", False)       

print(car1.model)  # Output: Clio Classique
print(car1.year)   # Output: 2007
print(car1.color)  # Output: Grey
print(car1.for_sale)  # Output: False

