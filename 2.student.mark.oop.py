class Student:
    def __init__(self, name, student_id, bod):
        self.name = name
        self.student_id = student_id
        self.bod = bod
        
class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        
class MarkSheet:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.marks = [[0 for _ in range(len(courses))]for _ in range(len(students))]
        
        def input_mark(self):
            while True:
                message = int(input("Input 1 to continue input or 0 to quit: "))
                if message == 1:
                    student_name = str(input("Choose a student: "))
                    course_name = str(input("Choose a course: "))
                    student_index = self.find_student_index(student_name)
                    course_index = self.find_course_index(course_name)

                    if student_index is None or course_index is None:
                        print("Invalid course's name or student's name. Try again.")
                    else:
                        self.mark_table[student_index][course_index] = input(
                            f"Enter mark of {self.classroom[student_index].student_name} in {self.courses[course_index].course_name}: ")
                elif message == 0:
                    break
                else:
                    print("Invalid Input. Try Again")
                    
def display_marks(self):
        while True:
            course_name = str(input("Choose a course: "))
            course_index = self.find_course_index(course_name)

            if course_index is None:
                print("Course not found, please try again.")
            else:
                banner_mark = "List of Marks: "
                for student in self.classroom:
                    banner_mark += f"{student.student_name} has {self.mark_table[self.classroom.index(student)][course_index]}, "
                banner_mark = banner_mark[:-2]
                print(banner_mark)

            choice = input("Enter 1 to view another course or 0 to exit: ")
            if choice != '1':
                break

def display_course(self):
    banner_course = f"There are {len(self.courses)} course(s) include: "
    for course in self.course:
        banner_course += course.course_name + ", "
    banner_course = banner_course[:-2]
    print(banner_course)
    
def display_students(self):
    banner_student = f"There are {len(self.classroom)} student(s) include: "
    for student in self.classroom:
        banner_student += student.student_name + ", "
    banner_student = banner_student[:-2]
    print(banner_student)
    
def find_student_index(self, student_name):
    for student in self.classroom:
        if student_name == student.student_name:
            return self.classroom.index(student)
    return None

def find_course_index(self, course_name):
    for course in self.courses:
        if course_name == course.course_name:
            return self.courses.index(course)
    return None

def input_students(num_students):
    classroom = []
    for i in range(num_students):
        student_id = input(f"Enter Student ID {i + 1}: ")
        student_name = input(f"Enter Student Name {i + 1}: ")
        student_dob = input(f"Enter Student DOB {i + 1}: ")
        student = Student(student_id, student_name, student_dob)
        classroom.append(student)
    return classroom
  
def input_courses(num_courses):
    courses = []  
    for i in range(num_courses):
        course_id = input(f"Enter Course ID {i + 1}: ") 
        course_name = input (f"Enter Course Name {i + 1}: ")   
        course = Course(course_id, course_name)
        courses.append(course)
    return courses

