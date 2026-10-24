# static methods are methods that belong to a class rather than an instance of the class (objects).
# They can be called on the class itself, without creating an instance of the class (object).
# Static methods are defined using the @staticmethod decorator.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"    
        
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Developer', 'Designer', 'Tester']
        return position in valid_positions

# here we can call the static method is_valid_position() on the class itself, without creating an instance of the class (object).
print(Employee.is_valid_position("Developer"))  # True
print(Employee.is_valid_position("Editor"))     # False 
print(Employee.is_valid_position("Manager"))    # True


employee1 = Employee("Qamro", "Developer")
employee2 = Employee("Raid", "Manager")
employee3 = Employee("Bassem", "Editor")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())