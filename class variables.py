class student:
    
    class_year = 2026 # this is the class variable it will be shared in all the student objects
    
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        



# creating objects of student class

student1 = student("Qamro", 18, "ESTIN")
print(student1.name)
print(student1.age)
print(student1.school)
print(student1.class_year)

print()

student2 = student("Ahmed", 18, "ESI Alger")
print(student2.name)
print(student2.age)
print(student2.school)        
print(student2.class_year)       