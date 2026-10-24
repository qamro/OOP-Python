# class methods are methods that belong to a class rather than an instance of the class (objects).
# They can be called on the class itself, without creating an instance of the class (object).
# Class methods are defined using the @classmethod decorator.

class Student:
    
    class_year = 2026 # this is the class variable, it will be shared among all the student class objects
    count = 0 # this is the class variable, it will be shared among all the student class objects
    
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        Student.count += 1 # increment the count of students when each object is created
        
    @classmethod
    def get_class_year(cls):  # we use cls instead of self to refer to the class itself not to refer to the object of the class
        return cls.class_year
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    
student1 = Student("Qamro", 20, "ESTIN")
student2 = Student("Raid", 21, "ESTIN")
student3 = Student("Bassem", 22, "ESTIN")    

print(Student.get_class_year())  # 2026
print(Student.get_count())  # 3