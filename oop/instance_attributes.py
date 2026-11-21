class Warrior:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print(f"I am {self.name}")
        print(f"My power is {self.power}")


ichigo = Warrior("Ichigo", "Getsuga Tensho")
rukia = Warrior("Rukia", "Sode no Shirayuki")

ichigo.introduce()
rukia.introduce()