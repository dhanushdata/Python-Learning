def create_lid(title):

    def show_lid():
        print(f"Lid : {title}")

    return show_lid

ichigo = create_lid("Ichigo")
rukia = create_lid("Rukia")

ichigo()
rukia()