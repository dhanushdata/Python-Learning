def check_age(age):

    if age >= 18:
        return "Adult"

    elif age >= 13:
        return "Teenager"

    else:
        return "Child"

result = check_age(int(input("Enter your age: ")))

print(result)