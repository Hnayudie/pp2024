import pickle
import gzip

class MarkSheet:
    def __init__(self, students, courses):
        self.students = students
        self.courses = courses
        self.marks = [[0 for _ in range(len(courses))] for _ in range(len(students))]

    def input_mark(self):
        for student in self.students:
            for course in self.courses:
                mark = float(input(f"Enter mark of {student.name} in {course.name}: "))
                student_index = self.students.index(student)
                course_index = self.courses.index(course)
                self.marks[student_index][course_index] = mark

    def calculate_gpa(self, student_name):
        student_index = self.find_student_index(student_name)
        if student_index is None:
            print("Student not found.")
            return

        total_credit = 0
        weighted_sum = 0

        for i, mark in enumerate(self.marks[student_index]):
            if mark != 0:
                course_credit = self.courses[i].credit
                total_credit += course_credit
                weighted_sum += mark * course_credit

        if total_credit == 0:
            print("No marks found for the student.")
            return

        gpa = weighted_sum / total_credit
        print(f"The GPA of {student_name} is: {gpa:.2f}")

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

    def save_marks(self, marks_file):
        with gzip.open(marks_file, "wb") as file:
            pickle.dump(self.marks, file)

    def load_marks(self, marks_file):
        with gzip.open(marks_file, "rb") as file:
            self.marks = pickle.load(file)
