class Warrior:
    organization = "Soul Society"

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My power is {self.power}")
        print(f"My Organization is {self.organization}")

ichigo = Warrior("Ichigo", "Getsuga")
rukia = Warrior("Rukia", "Ice")

ichigo.introduce()
rukia.introduce()
Warrior.organization = "Karakura Town"
print("\nAfter changing class attribute")



ichigo.introduce()
rukia.introduce()