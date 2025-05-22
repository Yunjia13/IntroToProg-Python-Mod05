# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Yunjia He,5/20/2025,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""
FILE_NAME: str = "Enrollments.json"


# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file: object = None
menu_choice: str = ""
student_data: dict
students: list = []

#Load data from file
import json

try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("File must exist before running this program!\n")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep= '\n')
    print("program ended!")
    quit()
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    print("program ended")
    quit()

# Present the menu of choices
while True:
    print(MENU)
    menu_choice = input("What would you like to do? ")
    print()

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("First name should not contain numbers!")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep= '\n')
            print()
            continue
        try:
            student_last_name = input("Enter the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("Last name should not contain numbers!")
        except ValueError as e:
            print(e)
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep= '\n')
            print()
            continue
        course_name = input("Please enter the course's name? ")
        student_data:dict = {"First_name": student_first_name,
                             "Last_name": student_last_name,
                             "Course": course_name}
        students.append(student_data)
        print()

# Present the current data
    elif menu_choice == "2":
        print("The current data is:")
        for student in students:
            print(f'{student["First_name"]}, '
                  f'{student["Last_name"]}, '
                  f'{student["Course"]}')
        print()

# Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent = 2)
            file.close()
            print("Data saved! The current data is:")
        except FileNotFoundError as e:
            print("File must exist before running this program!\n")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
            print("program ended!")
            quit()
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            print("program ended!")
            quit()
        for student in students:
            print(f'{student["First_name"]},'
                  f'{student["Last_name"]}, '
                  f'{student["Course"]}')
        print()

# Stop the loop
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1~4")
        print()
print("Program Ended")
