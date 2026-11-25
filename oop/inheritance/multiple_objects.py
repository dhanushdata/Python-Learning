class Creator:

    def __init__(self, username):
        self.username = username

    def show_profile(self):
        print(f"Creator: {self.username}")


username1 = input("Enter first creator username: ")
username2 = input("Enter second creator username: ")
username3 = input("Enter third creator username: ")

creator1 = Creator(username1)
creator2 = Creator(username2)
creator3 = Creator(username3)

print("\n--- Creator ---")

creator1.show_profile()
creator2.show_profile()
creator3.show_profile()