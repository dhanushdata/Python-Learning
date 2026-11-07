students = {
    "Dhanush": {"age": 16, "marks": [95, 88, 92]},
    "Arun": {"age": 17, "marks": [78, 85, 90]},
    "Vijay": {"age": 16, "marks": [91, 94, 89]}
}

for key, value in students.items():

    marks = value["marks"]
    total = 0

    for mark in marks:
        total = total + mark

    avg = total / len(marks)

    print(key, "avg is", avg)