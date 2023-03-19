import random

class Student:
    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_num}"

students = [
    Student("Alice", 20, "001"),
    Student("Bob", 22, "002"),
    Student("Charlie", 21, "008"),
    Student("Cents", 16, "214"),
    Student("Marco", 24, "099"),
    Student("Hanner", 9, "051"),
    Student("Migs", 12, "071"),
    Student("Dave", 100, "120"),
    Student("Cj", 20, "201")
]

# Shuffle the list of students
random.shuffle(students)

# Sort the list of students by age
students.sort(key=lambda x: x.id_num)

# Display all attributes of the sorted list of students
for student in students:
    print(student)