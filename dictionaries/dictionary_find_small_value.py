laptop = {
    "ram": 128,
    "storage": 4,
    "cores": 16,
    "threads": 32
}

smallest_value = None

for value in laptop.values():
    if smallest_value is None:
        smallest_value = value

    elif value < smallest_value:
        smallest_value = value

print(smallest_value)