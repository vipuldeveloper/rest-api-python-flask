### IMP: always use default as unmutable data type ###

from typing import List, Optional

class Stundent:
    def __init__(self, name: str, grades: Optional[List[int]] = None): #this is bad!
        self.name = name
        self.grades = grades or []
        
    def take_exam(self, result: int):
        self.grades.append(result)
    
    
vipul = Stundent("vipul")
vipul.take_exam(90)
print(vipul.grades)

kavar = Stundent("Kavar")
print(kavar.grades)