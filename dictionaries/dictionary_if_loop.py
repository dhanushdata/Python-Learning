laptop = {
    "brand": "lenovo",
    "ram": 128,
    "storage": 4,
    "processor": "AMD Ryzen 9 5900HX"
}

for key in laptop:
    if key == "ram":
        print("ram found")

    print(laptop[key])