from input import input_students, input_courses
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet
from output import display_courses, display_students, display_marks

def main():
    num_students = int(input("Enter the number of students (maximum 450): "))
    students = input_students(num_students)

    num_courses = int(input("Enter number of courses (maximum 50): "))
    courses = input_courses(num_courses)

    mark_sheet = MarkSheet(students, courses)
    mark_sheet.input_mark()

    display_courses(courses)
    display_students(students)
    display_marks(mark_sheet)

    student_name = input("Enter student name to calculate GPA: ")
    mark_sheet.calculate_gpa(student_name)

if __name__ == "__main__":
    main()
