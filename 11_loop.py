#if, elif, else
#for, while


# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if(number % 2 == 0):
        evens.append(number)
        
print(evens)