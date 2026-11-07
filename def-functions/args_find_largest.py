def largest_number(*number):

    largest_value = None

    for value in number:

        if largest_value is None:
            largest_value = value

        elif value > largest_value:
            largest_value = value

    return largest_value

result = largest_number(10, 20, 30)

print(result)