students = {
    "Dhanush": {"age": 16, "mark": 95},
    "Arun": {"age": 17, "mark": 88},
    "Vijay": {"age": 16, "mark": 91}
}

largest_value = None
largest_key = None

for key, value in students.items():

    if largest_value is None:
        largest_value = value["mark"]
        largest_key = key

    elif value["mark"] > largest_value:
        largest_value = value["mark"]
        largest_key = key

print("Top student is", largest_key, ":", largest_value)