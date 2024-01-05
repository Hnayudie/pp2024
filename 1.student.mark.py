# Global variables
mark_table = [] 
classroom = []
number_of_student = 0
id_student = 45
student_name = ""
Dob = ""
course = []
number_of_course = 0
id_course = 45
course_name = ""

# Input functions
def input_number_of_student():
    number_of_student = int(input("Enter the number of student (maximum 450): "))
    while True:
        if 0 < number_of_student < 450:
            break
        else:
            print("Why so many? Kill some and comeback later")
            number_of_student = int(input("Enter the number of student (maximum 450): "))
    return number_of_student

def input_student_info(x):
    while True:
        student_id = input(f"Student ID {x + 1}: ")
        if student_id.isalnum():
            break
        else:
            print("Invalid Student ID. Try again.")

    student_name = input(f"Enter Student Name {x + 1}: ")
    student_dob = input(f"Enter Student DOB {x + 1} (dd/mm/yyyy): ")
    temp1 = {'name': student_name, 'id': student_id, 'dob': student_dob}
    classroom.append(temp1)

        
def input_number_of_course():
    number_of_courses = int(input(f"Enter number of courses (maximum 50): "))
    while True:
        if 0 < number_of_courses < 50:
            break
        else:
            print("U are too studious. Try again.")
            number_of_courses = int(input(f"Enter number of Courses: "))
    return number_of_courses

def input_course_info(x):
    