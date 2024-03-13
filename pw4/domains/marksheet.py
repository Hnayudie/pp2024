import numpy as np
import math

class MarkSheet:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.marks = np.zeros((len(students), len(courses)))

    def input_mark(self):
        while True:
            message = int(input("Input 1 to continue input or 0 to quit: "))
            if message == 1:
                student_name = str(input("Choose a student: "))
                course_name = str(input("Choose a course: "))
                mark = math.floor(float(input(f"Enter mark of {student_name} in {course_name}: ")) * 10) / 10
                student_index = self.find_student_index(student_name)
                course_index = self.find_course_index(course_name)

                if student_index is None or course_index is None:
                    print("Invalid course's name or student's name. Try again.")
                else:
                    self.marks[student_index][course_index] = mark
            elif message == 0:
                break
            else:
                print("Invalid Input. Try Again")

    def display_marks(self):
        while True:
            course_name = str(input("Choose a course: "))
            course_index = self.find_course_index(course_name)

            if course_index is None:
                print("Course not found, please try again.")
            else:
                banner_mark = "List of Marks: "
                for student in self.students:
                    student_index = self.find_student_index(student.name)
                    banner_mark += f"{student.name} has {self.marks[student_index][course_index]}, "
                banner_mark = banner_mark[:-2]
                print(banner_mark)

            choice = input("Enter 1 to view another course or 0 to exit: ")
            if choice != '1':
                break

    def calculate_gpa(self, student_name):
        student_index = self.find_student_index(student_name)
        if student_index is None:
            print("Student not found.")
            return

        total_credit = 0
        weighted_sum = 0

        for i, mark in enumerate(self.marks[student_index]):
            if mark != 0:
                course_credit = self.courses[i].credit
                total_credit += course_credit
                weighted_sum += mark * course_credit

        if total_credit == 0:
            print("No marks found for the student.")
            return

        gpa = weighted_sum / total_credit
        print(f"The GPA of {student_name} is: {gpa:.2f}")

    def find_student_index(self, student_name):
        for student in self.students:
            if student_name == student.name:
                return self.students.index(student)
        return None

    def find_course_index(self, course_name):
        for course in self.courses:
            if course_name == course.name:
                return self.courses.index(course)
        return None
