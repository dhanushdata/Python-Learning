def student(name, *subjects, **details):

    print("Name", name)

    print("Subjects:")

    for subject in subjects:
        print(subject)

    print("Details:")

    for key, value in details.items():
        print(key, value)

student(
    "Dhanush",
    "Python",
    "German",
    "Maths",
    age=16,
    grade=11
)