import pickle
import gzip
from domains.student import Student
from domains.course import Course

def input_students(num_students, students_file):
    students = []
    for i in range(num_students):
        student_id = input(f"Enter Student ID {i + 1}: ")
        student_name = input(f"Enter Student Name {i + 1}: ")
        student_dob = input(f"Enter Student DOB {i + 1}: ")
        student = Student(student_name, student_id, student_dob)
        students.append(student)

    with open(students_file, "wb") as file:
        pickle.dump(students, file)

    return students
  
def input_courses(num_courses, courses_file):
    courses = []
    for i in range(num_courses):
        course_id = input(f"Enter Course ID {i + 1}: ")
        course_name = input(f"Enter Course Name {i + 1}: ")
        course_credit = float(input(f"Enter Course Credit {i + 1}: "))
        course = Course(course_name, course_id)
        course.credit = course_credit
        courses.append(course)

    with open(courses_file, "wb") as file:
        pickle.dump(courses, file)

    return courses

def input_marks(students, courses, marks_file):
    marks = []
    for student in students:
        student_marks = []
        for course in courses:
            mark = float(input(f"Enter mark of {student.name} in {course.name}: "))
            student_marks.append(mark)
        marks.append(student_marks)

    with gzip.open(marks_file, "wb") as file:
        pickle.dump(marks, file)
