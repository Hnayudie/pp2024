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

    with open(students_file, "w") as file:
        for student in students:
            file.write(f"{student.name},{student.student_id},{student.bod}\n")

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

    with open(courses_file, "w") as file:
        for course in courses:
            file.write(f"{course.name},{course.course_id},{course.credit}\n")

    return courses

def input_marks(num_students, num_courses, marks_file):
    with open(marks_file, "w") as file:
        for i in range(num_students):
            for j in range(num_courses):
                mark = float(input(f"Enter mark of Student {i+1} in Course {j+1}: "))
                file.write(f"{mark},")
            file.write("\n")
