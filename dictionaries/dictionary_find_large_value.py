laptop = {
    "ram": 128,
    "storage": 4,
    "cores": 16,
    "threads": 32
}

largest_value = None

for value in laptop.values():
    if largest_value is None:
        largest_value = value

    elif value > largest_value:
        largest_value = value

print(largest_value)