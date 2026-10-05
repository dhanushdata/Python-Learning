def calculate(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total

result = calculate(10, 20, 30)

print(result)