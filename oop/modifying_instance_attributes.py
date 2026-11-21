class Warrior:
    def __init__(self, name, power):
        self.name = name
        self.power = power


ichigo = Warrior("Ichigo", "Getsuga")
rukia = Warrior("Rukia", "Ice")

ichigo.power = "Final Getsuga"

print(ichigo.power)
print(rukia.power)