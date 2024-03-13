import os

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

        data_dir = os.path.join(os.path.dirname(__file__), "../data")
        marks_file = os.path.join(data_dir, "marks.txt")
        with open(marks_file, "w") as file:
            for student, student_marks in zip(self.students, self.marks):
                marks_str = ",".join([str(mark) for mark in student_marks])
                file.write(f"{student.name},{marks_str}\n")

    def display_marks(self):
        data_dir = os.path.join(os.path.dirname(__file__), "../data")
        marks_file = os.path.join(data_dir, "marks.txt")

        with open(marks_file, "r") as file:
            for line in file:
                student_name, marks_str = line.strip().split(",", 1)
                marks = marks_str.split(",")
                marks_info = ", ".join([f"{self.courses[i].name}: {marks[i]}" for i in range(len(marks))])
                print(f"{student_name}: {marks_info}")

    def calculate_gpa(self, student_name):
        student_index = None
        for student in self.students:
            if student.name == student_name:
                student_index = self.students.index(student)
                break

        if student_index is not None:
            total_credit = 0
            weighted_sum = 0
            for i, course in enumerate(self.courses):
                total_credit += course.credit
                weighted_sum += course.credit * self.marks[student_index][i]

            if total_credit == 0:
                print("Cannot calculate GPA. Total credits are zero.")
            else:
                gpa = weighted_sum / total_credit
                print(f"The GPA of {student_name} is: {gpa}")
        else:
            print("Student not found.")

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
