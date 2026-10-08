def warrior(name):
    power = 100

    def train():
        nonlocal power
        power = power + 50
        print(name, ":", power)

    return train

ichigo = warrior("Ichigo")
rukia = warrior("Rukia")

ichigo()
ichigo()
rukia()
ichigo()
rukia()