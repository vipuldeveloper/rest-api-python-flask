def addition(*args):
    print(args)

    total = 0
    for arg in args:
        total = total + arg
        
    return total