#to work typehint installed mypy package
# RUN USING mypy 28_typehinting.py

class Person:
    def __init__(self, name: str):
        self.name = name
        
    def getName(self):
        print('My name is {}'.format(self.name))
        
class Engineer(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.profession = "Engineer"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))
        
class Doctor(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.profession = "Doctor"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))

        
engineer = Engineer("Vipul")
engineer.getName()
#engineer.sayProfession()

# doctor = Doctor("Dilip")
# doctor.getName()
# doctor.sayProfession()