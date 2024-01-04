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
        
def main():
    # Input function: 
    num_students = int(input("Enter number of students: "))
    num_courses = int(input("Enter number of courses: "))
    
    # Students and courses List
    students = []
    courses = []
    
    # Input Students and Courses info
    for _ in range(num_students):
        student_name = input("Enter Student Name: ")
        student_id = int(input("Enter Student ID: "))
        student_dob = input("Enter Student DOB: ")
        marks = {course['id']: None for course in courses}
        students.append({'name': student_name, 'id': student_id, 'dob': student_dob})
        
    for _ in range(num_courses):
        course_name = input("Enter Course Name: ")
        course_id = int(input("Enter Course ID: "))
        courses.append({'name': course_name, 'id': course_id})
        blahblahS
        
        
        