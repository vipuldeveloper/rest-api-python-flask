# IMMUTABLE: int, str, bool, float, tuple

a = ()
b = a

print(id(a))
print(id(b))

# it will create new object
a = a + ("asda",)

print(id(a))
print(id(b))