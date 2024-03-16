import os
from input import input_students, input_courses
from domains.student import Student
from domains.course import Course
from domains.marksheet import MarkSheet
from output import display_courses, display_students, display_marks
from persistence import PersistenceManager
import gui

def main():
    data_dir = os.path.join(os.path.dirname(__file__), "data")

    persistence_manager = PersistenceManager(data_dir)

    students_file = "students.pkl"
    courses_file = "courses.pkl"
    marks_file = "marks.pkl.gz"

    students = persistence_manager.load_data(students_file)
    courses = persistence_manager.load_data(courses_file)

    if students is None:
        num_students = gui.get_num_students()
        students = input_students(num_students)
        persistence_manager.save_data(students_file, students)

    if courses is None:
        num_courses = gui.get_num_courses()
        courses = input_courses(num_courses)
        persistence_manager.save_data(courses_file, courses)

    mark_sheet = MarkSheet(students, courses)

    if not os.path.exists(os.path.join(data_dir, marks_file)):
        mark_sheet.input_mark()
        persistence_manager.save_data(marks_file, mark_sheet.marks)
    else:
        mark_sheet.marks = persistence_manager.load_data(marks_file)

    display_courses(courses)
    display_students(students)
    display_marks(mark_sheet)

    student_name = gui.get_student_name()
    mark_sheet.calculate_gpa(student_name)

if __name__ == "__main__":
    main()
