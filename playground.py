class Student:
    def __init__(self, name, mark):
        self.name = name 
        self.mark = mark

    def show_info(self):
        print("Name: ", self.name)
        print("Mark: ", self.mark)

    def update_info(self, new_mark):
        self.mark = new_mark

student1 = Student("Dinesh", 90)
student2 = Student("Mark Zuckerberg", 89)

student1.show_info()
student2.show_info()

student1.update_info(99)

print("\n")

student1.show_info()