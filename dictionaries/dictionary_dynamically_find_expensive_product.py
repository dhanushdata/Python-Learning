products = {}

for i in range(3):
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price: "))

    products[product_name] = product_price

print(products)

product_name = None
product_price = None

for key, value in products.items():

    if product_price is None:
        product_price = value
        product_name = key

    elif value > product_price:
        product_price = value
        product_name = key

print("Expensive product is", product_name, ":",product_price)