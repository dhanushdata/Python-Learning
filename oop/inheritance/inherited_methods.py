class User:

    def __init__(self, username):
        self.username = username

    def show_profile(self):
        print(f"Username: {self.username}")


class Creator(User):

    def upload_lid(self):
        print(f"{self.username} uploaded a Lid!")


username = input("Enter creator username: ")

creator1 = Creator(username)

print("\n--- Creator Activity ---")

creator1.show_profile()
creator1.upload_lid()