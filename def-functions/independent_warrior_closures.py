def warrior(name, power):
    def train(amount):
        nonlocal power
        power = power + amount
        print(name, ":", power)

    return train

ichigo = warrior("Ichigo", 100)
rukia = warrior("Rukia", 80)

ichigo(20)
ichigo(10)
rukia(10)
ichigo(-5)
rukia(-5)
ichigo(-10)
rukia(20)