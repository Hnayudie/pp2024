def get_student_marks(students, course_id):
    for student in students:
        print(f"{student['name']}: {student['marks'][course_id]}")

def input_student_marks(students, courses):
    for student in students:
        print(f"Enter marks for {student['name']}:")
        for course in courses:
            mark = float(input(f"Enter mark for course {course['name']}: "))
            student['marks'][course['id']] = mark

def list_students(students):
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")

def list_courses(courses):
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")