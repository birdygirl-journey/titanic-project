# ==========================
#  Student Record System
# ==========================
# This mini project lets you:
# ➤ Add student records
# ➤ View all records
# ➤ Search for a student
# ➤ Delete a student record
# ➤ Exit the program
# All data is stored in memory (not in a file) for simplicity.

# Create an empty list to store student records
students = []

# ---------------------------
# Function: Add a new student
# ---------------------------
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    grade = input("Enter class/grade: ")

    # Create a dictionary to hold one student's data
    student = {"Name": name, "Roll": roll, "Grade": grade}

    # Add this dictionary to the list
    students.append(student)
    print(" Student added successfully!\n")

# ------------------------------
# Function: View all students
# ------------------------------
def view_students():
    print("\n--- All Students ---")
    if len(students) == 0:
        print("⚠️ No records found!\n")
    else:
        # Loop through each student and print their details
        for s in students:
            print(f"Name: {s['Name']} | Roll: {s['Roll']} | Grade: {s['Grade']}")
        print()  # blank line

# --------------------------------------
# Function: Search for a student by roll
# --------------------------------------
def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number to search: ")

    # Loop through each record and find matching roll
    for s in students:
        if s["Roll"] == roll:
            print(f" Found: Name: {s['Name']} | Grade: {s['Grade']}\n")
            return  # stop searching once found
    print(" Student not found!\n")

# ---------------------------------
# Function: Delete a student record
# ---------------------------------
def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ")

    # Loop through list and remove matching record
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print(" Student record deleted!\n")
            return
    print(" Student not found!\n")

# -------------------------
# Main menu of the program
# -------------------------
def menu():
    while True:
        # Display menu options
        print("===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Call the correct function based on user choice
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print(" Exiting program... Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter 1–5.\n")

# -------------------------
# Run the program
# -------------------------
menu()
