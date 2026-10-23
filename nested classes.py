class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def display_info(self):
            return f"Employee Name: {self.name}, Position: {self.position}"
        
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
        
    def list_employees(self):
        return [employee.display_info() for employee in self.employees]    