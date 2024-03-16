import tkinter as tk
from tkinter import simpledialog

def get_num_students():
    root = tk.Tk()
    root.withdraw()
    num_students = simpledialog.askinteger("Number of Students", "Enter the number of students (maximum 450): ")
    root.destroy()
    return num_students

def get_student_info(num_students):
    students = []
    for i in range(num_students):
        student_id = get_student_id(f"Student {i+1} ID")
        student_name = simpledialog.askstring(f"Student {i+1} Name", f"Enter Student {i+1} Name: ")
        student_dob = simpledialog.askstring(f"Student {i+1} DOB", f"Enter Student {i+1} DOB: ")
        students.append((student_id, student_name, student_dob))
    return students

def get_student_id(title):
    root = tk.Tk()
    root.withdraw()
    student_id = simpledialog.askinteger(title, "Enter Student ID: ")
    root.destroy()
    return student_id

def get_num_courses():
    root = tk.Tk()
    root.withdraw()
    num_courses = simpledialog.askinteger("Number of Courses", "Enter the number of courses (maximum 50): ")
    root.destroy()
    return num_courses

def get_student_name():
    root = tk.Tk()
    root.withdraw()
    student_name = simpledialog.askstring("Student Name", "Enter student name to calculate GPA: ")
    root.destroy()
    return student_name
