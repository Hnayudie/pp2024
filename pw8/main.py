import os
from input import input_students, input_courses
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet
from output import display_courses, display_students, display_marks
from persistence import PersistenceManager

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")

    persistence_manager = PersistenceManager(data_dir)

    students_file = "students.pkl"
    courses_file = "courses.pkl"
    marks_file = "marks.pkl.gz"

    students = persistence_manager.load_data(students_file)
    courses = persistence_manager.load_data(courses_file)

    if students is None:
        num_students = int(input("Enter the number of students (maximum 450): "))
        students = input_students(num_students)
        persistence_manager.save_data(students_file, students)

    if courses is None:
        num_courses = int(input("Enter number of courses (maximum 50): "))
        courses = input_courses(num_courses)
        persistence_manager.save_data(courses_file, courses)

    mark_sheet = MarkSheet(students, courses)

    if not os.path.exists(os.path.join(data_dir, marks_file)):
        mark_sheet.input_mark()
        persistence_manager.save_data(marks_file, mark_sheet.marks)
    else:
        mark_sheet.marks = persistence_manager.load_data(marks_file)

    display_courses(courses)
    display_students(students)
    display_marks(mark_sheet)

    student_name = input("Enter student name to calculate GPA: ")
    mark_sheet.calculate_gpa(student_name)

if __name__ == "__main__":
    main()
