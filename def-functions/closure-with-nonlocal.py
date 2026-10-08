def create_warrior():
    power = 100

    def train():
        nonlocal power
        power = power + 20
        print(power)

    train()
    train()

    print(power)

create_warrior()