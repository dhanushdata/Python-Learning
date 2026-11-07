def calculate_average(*numbers):

    total = 0

    for value in numbers:
        total = total + value

    avg = total / len(numbers)

    return avg

result = calculate_average(95, 88, 92)

print(result)