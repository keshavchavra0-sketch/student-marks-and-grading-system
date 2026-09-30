students = []

subjects = ["Maths", "English", "Hindi", "Physics", "Chemistry"]


def find_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_valid_marks(subject):
    while True:
        try:
            marks = int(input("Enter marks in " + subject + ": "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks! Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def student_exists(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return True
    return False


def create_student(name, roll_no, marks):
    total = sum(marks.values())
    percentage = total / len(subjects)

    passed = True

    for subject in subjects:
        if marks[subject] < 40:
            passed = False

    grade = find_grade(percentage)

    if passed:
        result = "PASS"
    else:
        result = "FAIL"

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    return student


def display_student(student):
    print("\n------------------------------")
    print("Name       :", student["name"])
    print("Roll No    :", student["roll_no"])
    print("Total      :", student["total"], "/ 500")
    print("Percentage :", student["percentage"], "%")
    print("Grade      :", student["grade"])
    print("Result     :", student["result"])

    print("Subject Marks:")

    for subject in subjects:
        print(subject, ":", student["marks"][subject])


def add_student():
    print("\n========== ADD STUDENT ==========")

    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")

    if student_exists(roll_no):
        print("A student with this roll number already exists.")
        return

    marks = {}

    for subject in subjects:
        marks[subject] = get_valid_marks(subject)

    student = create_student(name, roll_no, marks)

    students.append(student)

    print("\nStudent added successfully!")
    display_student(student)


def display_students():
    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        display_student(student)


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            display_student(student)
            return

    print("Student not found.")


def update_student():
    print("\n========== UPDATE STUDENT ==========")

    roll_no = input("Enter roll number to update: ")

    for index in range(len(students)):

        if students[index]["roll_no"] == roll_no:

            name = input("Enter new name: ")

            marks = {}

            for subject in subjects:
                marks[subject] = get_valid_marks(subject)

            students[index] = create_student(name, roll_no, marks)

            print("\nStudent updated successfully!")
            display_student(students[index])
            return

    print("Student not found.")


def delete_student():
    print("\n========== DELETE STUDENT ==========")

    roll_no = input("Enter roll number to delete: ")

    for student in students:

        if student["roll_no"] == roll_no:
            students.remove(student)

            print("Student deleted successfully.")
            return

    print("Student not found.")


def class_summary():
    print("\n========== CLASS SUMMARY ==========")

    if len(students) == 0:
        print("No student records found.")
        return

    total_students = len(students)
    passed_students = 0
    failed_students = 0
    total_percentage = 0

    highest_percentage = students[0]["percentage"]
    top_student = students[0]["name"]

    for student in students:

        total_percentage = total_percentage + student["percentage"]

        if student["result"] == "PASS":
            passed_students = passed_students + 1
        else:
            failed_students = failed_students + 1

        if student["percentage"] > highest_percentage:
            highest_percentage = student["percentage"]
            top_student = student["name"]

    average = total_percentage / total_students

    print("Total Students :", total_students)
    print("Passed         :", passed_students)
    print("Failed         :", failed_students)
    print("Class Average  :", average, "%")
    print("Highest Score  :", highest_percentage, "%")
    print("Top Student    :", top_student)


while True:

    print("\n========================================")
    print("     STUDENT MARKS & GRADING SYSTEM")
    print("========================================")

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Summary")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        class_summary()

    elif choice == "7":
        print("\nThank you for using Student Marks & Grading System!")
        break

    else:
        print("\nInvalid choice! Please select 1 to 7.")
