
# lambda is short function without or with name
add = lambda x,y: x+y

print(add(5,7))



# actual usecases
def double(x):
    return x*2

sequence = [25,3,4,6]

#double = [double(x) for x in sequence]

# Using lambda function
#doubled = [(lambda x:x*2)(x) for x in sequence]

doubled = list(map(lambda x:x*2, sequence))
print(doubled)