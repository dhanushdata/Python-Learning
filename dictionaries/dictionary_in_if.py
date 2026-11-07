laptop = {
    "brand": "lenovo",
    "processor": "AMD Ryzen 9 5900HX",
    "gpu": "rtx 5090"
}

print("gpu" in laptop)
print("ram" in laptop)

if "gpu" in laptop:
    print("gpu is available")