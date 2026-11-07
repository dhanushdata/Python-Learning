def total(*number):

    total = 0

    for value in number:
        total = total + value

    return total

result = total(95, 88, 92)

print(result)