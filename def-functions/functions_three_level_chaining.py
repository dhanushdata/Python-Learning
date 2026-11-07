def add_five(number):
    return number + 5

def triple(number):
    return add_five(number) * 3

def subtract_four(number):
    return triple(number) - 4

print(subtract_four(6))