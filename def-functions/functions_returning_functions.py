def create_lid(title):
    def show_lid():
        print(f"Lid : {title}")

    return show_lid

my_lid = create_lid("Ichigo")

my_lid()