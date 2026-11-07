students = {
    "Dhanush": {"age": 16, "mark": 95},
    "Arun": {"age": 17, "mark": 88},
    "Vijay": {"age": 16, "mark": 91}
}

total = 0

for key, value in students.items():
    total = total + value["mark"]

avg = total / len(students)

print("avg mark is", avg)