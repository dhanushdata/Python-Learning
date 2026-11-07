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

for name, value in students.items():

    marks = value["marks"]
    total = 0

    for mark in marks:
        total = total + mark

    avg = total / len(marks)

    print(name, "average is", avg)