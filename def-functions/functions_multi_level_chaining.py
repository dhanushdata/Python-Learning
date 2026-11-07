def double(number):
    return number * 2

def add_ten(number):
    return double(number) + 10

def square(number):
    result = add_ten(number)
    return result * result

print(square(5))