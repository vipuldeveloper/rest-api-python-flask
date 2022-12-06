class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}")
        
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")
    
    @staticmethod
    def static_method():
        print(f"Called static method")

    def __str__(self):
        return f"Person is {self.name}"

        
# test = ClassTest()
# test.instance_method()
# ClassTest.instance_method(test)  

ClassTest.class_method()
ClassTest.static_method()