students = {
    "Dhanush": {
        "age": 16,
        "marks": [95, 88, 92]
    },
    "Arun": {
        "age": 17,
        "marks": [78, 85, 90]
    }
}

for name, data in students.items():

    print(name + ":")

    for mark in data["marks"]:
        print(mark)