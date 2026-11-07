students = {
    "Dhanush": {
        "age": 16,
        "mark": 95
    },
    "Arun": {
        "age": 17,
        "mark": 88
    },
    "Vijay": {
        "age": 16,
        "mark": 91
    }
}

for name, data in students.items():
    print(name, ":", data["age"], "years old")