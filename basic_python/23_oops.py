class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average(self):
        return sum(self.grades)/len(self.grades)
    

student  = Student("Vipul", (89,75,98,99))
print(student.name)
print(student.average())