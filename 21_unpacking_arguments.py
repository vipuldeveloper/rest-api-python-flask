def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
        
    return total


print(multiply(1, 3, 5))


# 2nd example, **as key as name and associated value as value
def add(x, y):
    return x+y

num = {"x":5, "y":2}
print(add(**num))

def sum(*args):
    totalSUM = 0
    for arg in args:
        totalSUM = totalSUM + arg
        
    return totalSUM

#3rd
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == '+':
        return sum(*args)
    else:
        return "No valid operator"
    
print(apply(1,4,5, operator="*"))


print("21_unpacking_arguments.py:", __name__)