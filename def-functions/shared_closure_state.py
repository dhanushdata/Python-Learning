def create_warrior(name):
    power = 100

    def train():
        nonlocal power
        power = power + 50
        print(name, "trained", power)

    def rest():
        nonlocal power
        power = power - 20
        print(name, "rested", power)

    return train, rest

train, rest = create_warrior("Ichigo")

train()
train()
rest()
train()
rest()