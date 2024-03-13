import os
import gzip
from input import input_students, input_courses
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet
from output import display_courses, display_students, display_marks

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    students_file = os.path.join(data_dir, "students.txt")
    courses_file = os.path.join(data_dir, "courses.txt")
    
    if os.path.exists(os.path.join(data_dir, "students.dat")):
        decompress_data(data_dir)

    num_students = int(input("Enter the number of students (maximum 450): "))
    students = input_students(num_students, students_file)

    num_courses = int(input("Enter number of courses (maximum 50): "))
    courses = input_courses(num_courses, courses_file)

    mark_sheet = MarkSheet(students, courses)
    mark_sheet.input_mark()

    display_courses(courses)
    display_students(students)
    display_marks(mark_sheet)

    student_name = input("Enter student name to calculate GPA: ")
    mark_sheet.calculate_gpa(student_name)

    compress_data(data_dir)

def load_students_from_file(students_file):
    students = []
    with open(students_file, "r") as file:
        for line in file:
            name, student_id, bod = line.strip().split(",")
            student = Student(name, student_id, bod)
            students.append(student)
    return students

def load_courses_from_file(courses_file):
    courses = []
    with open(courses_file, "r") as file:
        for line in file:
            name, course_id, credit = line.strip().split(",")
            course = Course(name, course_id)
            course.credit = float(credit)
            courses.append(course)
    return courses

def compress_data(data_dir):
    with open(os.path.join(data_dir, "students.txt"), "rb") as f_in:
        with gzip.open(os.path.join(data_dir, "students.dat"), "wb") as f_out:
            f_out.writelines(f_in)

    with open(os.path.join(data_dir, "courses.txt"), "rb") as f_in:
        with gzip.open(os.path.join(data_dir, "courses.dat"), "wb") as f_out:
            f_out.writelines(f_in)

def decompress_data(data_dir):
    with gzip.open(os.path.join(data_dir, "students.dat"), "rb") as f_in:
        with open(os.path.join(data_dir, "students.txt"), "wb") as f_out:
            f_out.writelines(f_in)

    with gzip.open(os.path.join(data_dir, "courses.dat"), "rb") as f_in:
        with open(os.path.join(data_dir, "courses.txt"), "wb") as f_out:
            f_out.writelines(f_in)

if __name__ == "__main__":
    main()
