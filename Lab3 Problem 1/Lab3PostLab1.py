"""
File: Lab3PostLab1.py

"""

from student import Student

def main():
    student1 = Student("Juan", 50)
    student2 = Student("Hannah", 50)
    print("Student 1 name:", student1.name)
    print("Student 2 name:", student2.name)
    print("Student 1 == Student 2:", student1 == student2)
    print("Student 1 < Student 2:", student1 < student2)
    print("Student 1 >= Student 2:", student1 >= student2)

if __name__ == "__main__":
    main()
