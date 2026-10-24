# static methods are methods that belong to a class rather than an instance of the class (objects).
# They can be called on the class itself, without creating an instance of the class (object).
# Static methods are defined using the @staticmethod decorator.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Developer', 'Designer', 'Tester']
        return position in valid_positions
    
    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
