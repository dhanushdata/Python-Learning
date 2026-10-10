def warrior(name, power):

    def train(amount):
        nonlocal power
        power = power + amount

    def show_power():
        print(name, ":", power)

    return train, show_power

rukia_train, rukia_show = warrior("Rukia", 80)

rukia_show()

rukia_train(10)
rukia_show()

rukia_train(20)
rukia_show()

rukia_train(-10)
rukia_show()