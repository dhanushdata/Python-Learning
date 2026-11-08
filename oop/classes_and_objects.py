class warrior:
    def introduce(self):
        print(f"I am {self.name}")


ichigo = warrior()
rukia = warrior()

ichigo.name = "Ichigo"
rukia.name = "Rukia"

ichigo.introduce()
rukia.introduce()