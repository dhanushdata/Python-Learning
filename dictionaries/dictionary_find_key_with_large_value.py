laptop = {
    "ram": 128,
    "storage": 4,
    "cores": 16,
    "threads": 32
}

large_value = None
large_key = None

for key, value in laptop.items():
    if large_value is None:
        large_value = value
        large_key = key

    elif value > large_value:
        large_value = value
        large_key = key

print(large_key, ":", large_value)