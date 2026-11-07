def subtract_three(number):
    return number - 3

def multiply_by_four(number):
    result = subtract_three(number)
    return result * 4

def add_two(number):
    result = multiply_by_four(number)
    return result + 2

print(add_two(10))