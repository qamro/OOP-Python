# multiple inheritance means that a class can inherit from multiple classes

class student:
    def __init__(self, name):
        self.name = name
        
    def student_info(self):
        print(f"Student name is {self.name}")

class teacher:
    def __init__(self, name):
        self.name = name

    def teacher_info(self):
        print(f"Teacher name is {self.name}")

class school(student, teacher):
    def description(self):
        self.student_info()
        self.teacher_info()