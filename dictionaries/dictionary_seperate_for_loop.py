laptop = {
    "brand": "lenovo",
    "ram": 128,
    "storage": 4,
    "processor": "AMD Ryzen 9 5900HX"
}

for key in laptop.keys():
    print(key)

for value in laptop.values():
    print(value)

for key, value in laptop.items():
    print(key, ":", value)