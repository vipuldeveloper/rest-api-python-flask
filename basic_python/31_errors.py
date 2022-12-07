def divide(dividend, divisor):
    if divisor == 0:
      raise ZeroDivisionError("Divisor cannot be 0")      
            
    return dividend/divisor

students = [
    {"name":"vipul", "grades":[50,60,70]},
    {"name":"kavar", "grades":[]},
    {"name":"nikunj", "grades":[60,70]}
]


try:
    for student in students:  
        name = student['name']  
        average = divide(sum(student['grades']), len(student['grades']))
        print(f"{name}'s avarage is: {average}")
except ZeroDivisionError as e:
    print(f"{name} has no grades!")
except ValueError as e:
    print(e)
else:
    print("---All studet averages calculate!--")
finally:
    print("--End of student average calculation---")