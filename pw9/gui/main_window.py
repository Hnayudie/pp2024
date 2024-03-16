import tkinter as tk
from tkinter import messagebox
from gui.persistence_manager import PersistenceManager
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Marksheet System")
        self.geometry("400x300")

        self.persistence_manager = PersistenceManager("data/")

        self.students_file = "students.pkl"
        self.courses_file = "courses.pkl"
        self.marks_file = "marks.pkl.gz"

        self.students = self.persistence_manager.load_data(self.students_file)
        self.courses = self.persistence_manager.load_data(self.courses_file)

        if self.students is None:
            self.create_students()
        
        if self.courses is None:
            self.create_courses()

        self.mark_sheet = MarkSheet(self.students, self.courses)

        if not self.persistence_manager.check_file_exists(self.marks_file):
            self.create_marks()

        self.display_buttons()

    def create_students(self):
        num_students = int(input("Enter the number of students (maximum 450): "))
        self.students = []
        for _ in range(num_students):
            student_id = input("Enter Student ID: ")
            student_name = input("Enter Student Name: ")
            student_dob = input("Enter Student DOB: ")
            student = Student(student_name, student_id, student_dob)
            self.students.append(student)
        self.persistence_manager.save_data(self.students_file, self.students)

    def create_courses(self):
        num_courses = int(input("Enter the number of courses (maximum 50): "))
        self.courses = []
        for _ in range(num_courses):
            course_id = input("Enter Course ID: ")
            course_name = input("Enter Course Name: ")
            course_credit = float(input("Enter Course Credit: "))
            course = Course(course_name, course_id)
            course.credit = course_credit
            self.courses.append(course)
        self.persistence_manager.save_data(self.courses_file, self.courses)

    def create_marks(self):
        self.mark_sheet.input_mark()
        self.persistence_manager.save_data(self.marks_file, self.mark_sheet.marks)

    def display_buttons(self):
        btn_create_students = tk.Button(self, text="Create Students", command=self.create_students)
        btn_create_students.pack()

        btn_create_courses = tk.Button(self, text="Create Courses", command=self.create_courses)
        btn_create_courses.pack()

        btn_create_marks = tk.Button(self, text="Create Marks", command=self.create_marks)
        btn_create_marks.pack()

        btn_display_marks = tk.Button(self, text="Display Marks", command=self.display_marks)
        btn_display_marks.pack()

    def display_marks(self):
        message = "List of Marks:\n"
        for student in self.students:
            for course in self.courses:
                mark = self.mark_sheet.get_mark(student, course)
                message += f"{student.name} has {mark} in {course.name}\n"
        messagebox.showinfo("Marks", message)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
