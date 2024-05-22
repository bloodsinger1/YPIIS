from datetime import date
from prettytable import PrettyTable

class Student:
    def __init__(self, first_name, last_name, birth_date, gradebook):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gradebook = gradebook

class Grade:
    def __init__(self, subject, exam_date, teacher_name, grade):
        self.subject = subject
        self.exam_date = exam_date
        self.teacher_name = teacher_name
        self.grade = grade

def has_failing_grade(gradebook):
    return any(grade.grade < 3 for grade in gradebook)

def print_failing_students(students):
    table = PrettyTable()
    table.field_names = ["First Name", "Last Name", "Birth Date"]
    for student in students:
        if has_failing_grade(student.gradebook):
            table.add_row([student.first_name, student.last_name, student.birth_date])
    print(table)

# Example usage:
students = [
    Student("John", "Doe", date(2000, 5, 15), [Grade("Math", date(2022, 5, 20), "Prof. Smith", 2)]),
    Student("Jane", "Doe", date(2001, 6, 25), [Grade("Math", date(2022, 5, 20), "Prof. Smith", 4)])
]

print_failing_students(students)

