class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def show_profile(self):
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")


class Creator(User):
    pass


username = input("Enter your Username!: ")
email = input("Enter your Email: ")

creator1 = Creator(username, email)

print("\nYour Profile")

creator1.show_profile()