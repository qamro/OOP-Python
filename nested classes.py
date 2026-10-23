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
    
company = Company("Alg Tech")

company.add_employee("Qamro", "AI Engineer")
company.add_employee("Amine", "Security Engineer")
company.add_employee("Bassem", "DevOps Engineer")
company.add_employee("Raid", "Data Scientist")


company2 = Company("Qamro Startup")
company2.add_employee("Qamro", "CEO")
company2.add_employee("Amine", "Technical Manager")
company2.add_employee("Bassem", "IT Specialist")

for employee in company.list_employees():
    print(employee)

print()

for employee in company2.list_employees():
    print(employee)