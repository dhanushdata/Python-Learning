class Warrior:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    #instance method 1
    def show_name(self):
        print(f"I am {self.name}")

    #instance method 2
    def show_power(self):
        print(f"My power is {self.power}")

    #instance method 3
    def change_power(self, new_power):
        self.power = new_power

ichigo = Warrior("Ichigo", "Getsuga")
ichigo.show_name()
ichigo.show_power()

ichigo.change_power("Final Getsuga")

ichigo.show_power()