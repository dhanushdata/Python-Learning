def number():
    power = 100

    def train():
        nonlocal power
        power = power + 20
        print(power)

    train()
    train()

    print(power)

number()