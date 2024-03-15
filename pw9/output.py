def display_courses(courses):
    banner_course = f"There are {len(courses)} course(s) include: "
    for course in courses:
        banner_course += course.name + ", "
    banner_course = banner_course[:-2]
    print(banner_course)

def display_students(students):
    banner_student = f"There are {len(students)} student(s) include: "
    for student in students:
        banner_student += student.name + ", "
    banner_student = banner_student[:-2]
    print(banner_student)

def display_marks(mark_sheet):
    while True:
        course_name = str(input("Choose a course: "))
        course_index = mark_sheet.find_course_index(course_name)

        if course_index is None:
            print("Course not found, please try again.")
        else:
            banner_mark = "List of Marks: "
            for student in mark_sheet.students:
                student_index = mark_sheet.find_student_index(student.name)
                banner_mark += f"{student.name} has {mark_sheet.marks[student_index][course_index]}, "
            banner_mark = banner_mark[:-2]
            print(banner_mark)

        choice = input("Enter 1 to view another course or 0 to exit: ")
        if choice != '1':
            break
