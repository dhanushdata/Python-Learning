laptop = {
    "brand": "lenovo",
    "ram": "128gb",
    "storage": "4tb",
    "processor": "AMD Ryzen 9 5900HX",
    "gpu": "rtx 5090"
}

laptop.pop("storage")
del laptop["ram"]
print(laptop)