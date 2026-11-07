products = {
    "laptop": {"price": 75000, "stock": 5},
    "phone": {"price": 30000, "stock": 8},
    "tablet": {"price": 45000, "stock": 3},
    "keyboard": {"price": 5000, "stock": 12}
}

highest_value = None
highest_product = None

for key, value in products.items():

    calculated_value = value["price"] * value["stock"]

    print(key, calculated_value)

    if highest_value is None:
        highest_value = calculated_value
        highest_product = key

    elif calculated_value > highest_value:
        highest_value = calculated_value
        highest_product = key

print("Highest inventory value is", highest_product, highest_value)