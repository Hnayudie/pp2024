import math
import numpy as np

class Student:
    def __init__(self, name, student_id, bod):
        self.name = name
        self.student_id = student_id
        self.bod = bod
        self.marks = []

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.credit = 0

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

    def display_courses(self):
        banner_course = f"There are {len(self.courses)} course(s) include: "
        for course in self.courses:
            banner_course += course.name + ", "
        banner_course = banner_course[:-2]
        print(banner_course)

    def display_students(self):
        banner_student = f"There are {len(self.students)} student(s) include: "
        for student in self.students:
            banner_student += student.name + ", "
        banner_student = banner_student[:-2]
        print(banner_student)

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

    def sort_students_by_gpa(self):
        student_gpas = []

        for student in self.students:
            student_index = self.find_student_index(student.name)
            total_credit = 0
            weighted_sum = 0

            for i, mark in enumerate(self.marks[student_index]):
                if mark != 0:
                    course_credit = self.courses[i].credit
                    total_credit += course_credit
                    weighted_sum += mark * course_credit

            if total_credit != 0:
                gpa = weighted_sum / total_credit
                student_gpas.append((student.name, gpa))

        sorted_student_gpas = sorted(student_gpas, key=lambda x: x[1], reverse=True)

        print("Sorted Students by GPA:")
        for name, gpa in sorted_student_gpas:
            print(f"{name}: {gpa:.2f}")

def input_students(num_students):
    students = []
    for i in range(num_students):
        student_id = input(f"Enter Student ID {i + 1}: ")
        student_name = input(f"Enter Student Name {i + 1}: ")
        student_dob = input(f"Enter Student DOB {i + 1}: ")
        student = Student(student_name, student_id, student_dob)
        students.append(student)
    return students

def input_courses(num_courses):
    courses = []
    for i in range(num_courses):
        course_id = input(f"Enter Course ID {i + 1}: ")
        course_name = input(f"Enter Course Name {i + 1}: ")
        course_credit = float(input(f"Enter Course Credit {i + 1}: "))
        course = Course(course_name, course_id)
        course.credit = course_credit
        courses.append(course)
    return courses

def main():
    num_students = int(input("Enter the number of students (maximum 450): "))
    students = input_students(num_students)

    num_courses = int(input("Enter number of courses (maximum 50): "))
    courses = input_courses(num_courses)

    mark_sheet = MarkSheet(students, courses)
    mark_sheet.input_mark()
    mark_sheet.display_courses()
    mark_sheet.display_students()
    mark_sheet.display_marks()

    student_name = input("Enter student name to calculate GPA: ")
    mark_sheet.calculate_gpa(student_name)

    mark_sheet.sort_students_by_gpa()


if __name__ == "__main__":
    main()
