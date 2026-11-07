def subtract_two(number):
    return number - 2

def square(number):
    result = subtract_two(number)
    return result * result

def add_five(number):
    return square(number) + 5

print(add_five(8))