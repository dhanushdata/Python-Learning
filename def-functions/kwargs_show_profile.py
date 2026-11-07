def show_profile(**numbers):

    for key, value in numbers.items():
        print(key, value)

show_profile(
    name = "Dhanush",
    age = 16,
    country = "Germany",
    goal = "Lot of goals"
)