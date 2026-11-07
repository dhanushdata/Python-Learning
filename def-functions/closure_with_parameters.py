def create_warrior(name, starting_power):
    power = starting_power

    def train(amount):
        nonlocal power
        power += amount
        print(name, power)

    return train

ichigo = create_warrior("Ichigo", 100)
rukia = create_warrior("Rukia", 80)

ichigo(30)
ichigo(50)
rukia(20)
ichigo(10)