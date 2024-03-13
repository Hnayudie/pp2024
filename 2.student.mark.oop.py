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
        self.marks = [[0 for _ in range(len(courses))] for _ in range(len(students))]

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
                    self.marks[student_index][course_index] = input(
                        f"Enter mark of {self.students[student_index].name} in {self.courses[course_index].name}: "
                    )
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
                for student in self.students:
                    banner_mark += f"{student.name} has {self.marks[self.find_student_index(student.name)][course_index]}, "
                banner_mark = banner_mark[:-2]
                print(banner_mark)

            choice = input("Enter 1 to view another course or 0 to exit: ")
            if choice != '1':
                break

    def display_courses(self):
        if not self.courses:
            print("No courses found.")
        else:
            banner_course = f"There are {len(self.courses)} course(s) include: "
            for course in self.courses:
                banner_course += course.name + ", "
            banner_course = banner_course[:-2]
            print(banner_course)

    def display_students(self):
        if not self.students:
            print("No students found.")
        else:
            banner_student = f"There are {len(self.students)} student(s) include: "
            for student in self.students:
                banner_student += student.name + ", "
            banner_student = banner_student[:-2]
            print(banner_student)

    def find_student_index(self, student_name):
        for student in self.students:
            if student_name == student.name:
                return self.students.index(student)
        return None

    def find_course_index(self, course_name):
        for course in self.courses:
            if course_name == course.name:
                return self.courses.index(course)
        return None


def input_students(num_students):
    classroom = []
    for i in range(num_students):
        student_id = input(f"Enter Student ID {i + 1}: ")
        student_name = input(f"Enter Student Name {i + 1}: ")
        student_dob = input(f"Enter Student DOB {i + 1}: ")
        student = Student(student_name, student_id, student_dob)
        classroom.append(student)
    return classroom
  
def input_courses(num_courses):
    courses = []  
    for i in range(num_courses):
        course_id = input(f"Enter Course ID {i + 1}: ") 
        course_name = input(f"Enter Course Name {i + 1}: ")   
        course = Course(course_name, course_id)
        courses.append(course)
    return courses

def main():
    num_students = int(input("Enter the number of students (maximum 450): "))
    classroom = input_students(num_students)
    
    num_courses = int(input("Enter number of courses (maximum 50): "))
    courses = input_courses(num_courses)
    
    mark_sheet = MarkSheet(classroom, courses)
    mark_sheet.input_mark()
    mark_sheet.display_courses()
    mark_sheet.display_students()
    mark_sheet.display_marks()
    
if  __name__=="__main__":
    main()
