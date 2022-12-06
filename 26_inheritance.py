# inheriting property of parent class

    # Types of Inheritance
    # single
    # Multiple
    # Multilevel
    # Hierarichal
    # Hybrid
    
#single: just give parent class name in parenthesis of child class
#multiple: just give parent classes name comma(,) separated in parenthesis of child class
#multilevel: second class inherits from a first class, 3rd class inherits second class.
#hierarichal: single class inherited into multiple classes, like sibling
#hybrid: Combination of any two kinds of inheritance

# IMP: use super function to access method of parent class
    # exmaple: super.parentClassMethod()
    
# Two main thing in inheritance
    # Overloading: same function different parameters
    # Overriding:  same function, same parameter, when want to change implemetion of super class
    
    
    
from ast import arg


class Person:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        print('My name is {}'.format(self.name))
        
class Engineer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Engineer"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))
        
class Doctor(Person):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Doctor"
    
    def sayProfession(self):
        print("My profession is {}".format(self.profession))

        
engineer = Engineer("Vipul")
engineer.getName()
engineer.sayProfession()

doctor = Doctor("Dilip")
doctor.getName()
doctor.sayProfession()

# How to avoid Overriding by multiple args with smartly 
def add(*args):
    if(len(args) == 2): return args[0] + args[1]
    result = 0
    for x in args:
        result += x
    return result

print(add(2,3)) 
print(add(2,3,4)) 
print(add(2,3,4,5)) 