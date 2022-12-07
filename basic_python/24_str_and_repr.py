class Person:
    def __init__(self, name):
        self.name = name
    
    
    # def __str__(self):
    #     return f"Person is {self.name}"
    
    def __repr__(self):
        return f"<Person('{self.name}')>"
    
vipul = Person("Vipul")
print(vipul)