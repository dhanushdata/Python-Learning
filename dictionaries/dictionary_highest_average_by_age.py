students = {
    "Dhanush": {"age": 16, "marks": [95, 88, 92]},
    "Arun": {"age": 17, "marks": [78, 85, 90]},
    "Vijay": {"age": 16, "marks": [91, 94, 89]},
    "Karthik": {"age": 17, "marks": [82, 79, 87]}
}

highest_average = None
highest_student = None

for key, value in students.items():

    if value["age"] == 16:
        marks = value["marks"]
        total = 0

        for mark in marks:
            total = total + mark

        avg = total / len(marks)

        if highest_average is None:
            highest_average = avg
            highest_student = key

        elif avg > highest_average:
            highest_average = avg
            highest_student = key

print(highest_student, highest_average)