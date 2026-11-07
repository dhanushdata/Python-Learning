product = {}

for i in range(3):
    product_name = input("Enter product name: ")
    product_price = int(input("Enter product price: "))

    product[product_name] = product_price

print(product)