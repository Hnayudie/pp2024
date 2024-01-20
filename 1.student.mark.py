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
        student_id = input(f"Enter Student ID {x + 1}: ")
        if student_id.isalnum():
            break
        else:
            print("Invalid Student ID. Try again.")

    student_name = input(f"Enter Student Name {x + 1}: ")
    student_dob = input(f"Enter Student DOB {x + 1} (dd/mm/yyyy): ")
    temp1 = {'student_name': student_name, 'student_id': student_id, 'student_dob': student_dob}
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
    while True:
        course_id = input(f"Enter Course ID {x + 1}: ")
        if course_id.isalnum():
            break
        else:
            print("Invalid Course ID. Try again.")
        
    course_name = input(f"Enter Course Name {x + 1}: ")
    temp2 = {'course_name': course_name, 'id': course_id}
    course.append(temp2)
    
def input_mark():
    mark = [[0 for _ in range(number_of_student)] for _ in range(number_of_course)]
    while True:
        while True:
            message = int(input("Input 1 to continue or 0 to quit: "))
            if message == 1:
                temp_student_name = str(input("Choose a student: "))
                temp_course_name = str(input("Choose a course:  "))
                count1, count2 = 0, 0 
                for x in range(number_of_course):
                    if temp_course_name == course[x]['course_name']:
                        count1 += 1
                        a = x
                for x in range(number_of_student):
                    if temp_student_name == classroom[x]['student_name']:
                        count2 += 2
                        b = x
                        
                if count1 == 0 or count2 == 0:
                    print("Invalid course's name or student's name. Try again.")
                else:
                    mark[b][a] = input(f"Enter mark of {classroom[b]['student_name']} in {course[a]['course_name']}: ")
            elif message == 0:
                return mark
            else:
                print("Invalid Input. Try Again")

# Display function    
def course_list():
    banner_course = f"There are {number_of_courses} course(s) include: "
    for x in range(number_of_courses):
        banner_course += course[x]['course_name'] + ", "
    banner_course = banner_course[:-2]
    print(banner_course)
    
def student_list():
    banner_student = f"There are {number_of_student} student(s) include: "
    for x in range(number_of_student):
        banner_student += classroom[x]['student_name'] + ", "
        banner_student = banner_student[:-2] 
        print(banner_student)
        
def mark_display(mark_table):
    while True:
        course_to_choose = str(input("Choose a course: "))
        course_chosen = 0
        for x in range(number_of_course):
            if course_to_choose == course[x]['course_name']:
                course_chosen += 1
                c = x
        if course_chosen == 0:
            print("Course not found, please try again.")
        else:
            banner_mark = "List of Mark: "
            for x in range(number_of_student):
                banner_mark += f"{classroom[x]['student name']} is {mark_table[c][x]}, "
            banner_mark = banner_mark[:-2]
            print(banner_mark)
        
        choice = input("Enter 1 to view another course or 0 to exit: ")
        if choice == '1':
            continue
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please Enter 1 or 0.")
            
# Main function
def main():
    number_of_student = input_number_of_student()
    for x in range(number_of_student):
        input_student_info(x)
        
    number_of_course = input_number_of_course()
    for x in range(number_of_course):
        input_course_info(x)
        
    mark_table = input_mark()
    course_list()
    student_list()
    mark_display(mark_table)