def get_price():
    return 100

def add_tax(price):
    result = price
    return result + 18

def check_price(price):

    if price >= 110:
        return "Teur"

    else:
        return "Billig"

price = get_price()
price = add_tax(price)
result = check_price(price)

print(result)