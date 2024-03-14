import os
import gzip
import pickle
from input import input_students, input_courses
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet
from output import display_courses, display_students, display_marks

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    students_file = os.path.join(data_dir, "students.pkl")
    courses_file = os.path.join(data_dir, "courses.pkl")
    marks_file = os.path.join(data_dir, "marks.pkl.gz")
    
    if os.path.exists(students_file):
        students = load_students_from_file(students_file)
    else:
        num_students = int(input("Enter the number of students (maximum 450): "))
        students = input_students(num_students, students_file)

    if os.path.exists(courses_file):
        courses = load_courses_from_file(courses_file)
    else:
        num_courses = int(input("Enter number of courses (maximum 50): "))
        courses = input_courses(num_courses, courses_file)
    
    mark_sheet = MarkSheet(students, courses)

    if os.path.exists(marks_file):
        mark_sheet.load_marks(marks_file)
    else:
        mark_sheet.input_mark()
        mark_sheet.save_marks(marks_file)

    display_courses(courses)
    display_students(students)
    display_marks(mark_sheet)

    student_name = input("Enter student name to calculate GPA: ")
    mark_sheet.calculate_gpa(student_name)

def load_students_from_file(students_file):
    with open(students_file, "rb") as file:
        students = pickle.load(file)
    return students

def load_courses_from_file(courses_file):
    with open(courses_file, "rb") as file:
        courses = pickle.load(file)
    return courses

if __name__ == "__main__":
    main()
