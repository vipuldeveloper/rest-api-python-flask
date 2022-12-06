from ctypes import Union


friends = {"Nikunj", "Vaibhav", "Kavar"}
abroad = {"Kavar"}

local_friends = friends.difference(abroad)
print(local_friends)

common = friends.intersection(abroad)
print(common)

##############################################################################
# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [30,20,50]

# Create a tuple, called my_tuple, with a single value in it
my_tuple = (20,)

# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8,7}
set2 = {5,7,9,12}

res = set1.intersection(set2)
print(res)
