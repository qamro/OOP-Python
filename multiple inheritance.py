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
    def __init__(self, student_name, teacher_name):
        student.__init__(self, student_name)
        teacher.__init__(self, teacher_name)