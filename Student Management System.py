import re  # Importing the regular expressions module for pattern matching

import certifi  # Importing certifi to use for secure connections with SSL certificates
from pymongo import MongoClient  # Importing MongoClient from pymongo to interact with MongoDB

# Establishing a connection to the MongoDB database using the provided connection string and SSL certificate
client = MongoClient("mongodb+srv://lezgo652:rikcy123@sms.wg2kx.mongodb.net/?ssl=true",  # MongoDB connection string with SSL enabled
                     tlsCAFile=certifi.where())  # Using certifi to locate the CA certificates for secure connection
print("Connected to MongoDB")  # Confirming successful connection to MongoDB

# Defining the databases and collections for students and teachers

database = client["STUDENTS"]  # Accessing the 'STUDENTS' database
students_enrolled = database["regular"]  # Collection for regularly enrolled students in the 'STUDENTS' database
irregular_student_enrolled = database["irregular"]  # Collection for irregularly enrolled students in the 'STUDENTS' database

database2 = client["TEACHERS"]  # Accessing the 'TEACHERS' database
teacher_in_db = database2["teacher"]  # Collection for regular teachers in the 'TEACHERS' database
sub_teacher_in_db = database2["SubTeacher"]  # Collection for substitute teachers in the 'TEACHERS' database

database3 = client["MAINUSERS"]  # Accessing the 'MAINUSERS' database
admin_in_db = database3["users"]  # Collection for admin users in the 'MAINUSERS' database

grade = 0  # Initializing a variable to store the grade, set to 0 initially

# Year 11 First Semester Subject Codes
a = "SH-CP 1"  # Computer Programming 1
b = "SH-ENGL 1"  # English 1
c = "SH-FIL 1"  # Filipino 1
d = "SH-HS 1"  # Hardware and Servicing 1
e = "SH-MATH 1"  # Mathematics 1
f = "SH-PE 1"  # Physical Education 1
g = "SH-SOCSCI 1"  # Social Science 1
h = "SH-SOCSCI 2"  # Social Science 2
i = "SH-SOCSCI 4"  # Social Science 4

# Year 11 Second Semester Subject Codes
j = "SH-CP 2"  # Computer Programming 2
k = "SH-ENGL 2"  # English 2
l = "SH-ETECH"  # Engineering Technology
m = "SH-FIL 2"  # Filipino 2
n = "SH-HS 2"  # Hardware and Servicing 2
o = "SH-MATH 2"  # Mathematics 2
p = "SH-PE 2"  # Physical Education 2
q = "SH-RES 1"  # Research 1
r = "SH-SOCSCI 3"  # Social Science 3

# Year 12 First Semester Subject Codes
s = "SH-CP 3"  # Computer Programming 3
t = "SH-ENGL 3"  # English 3
u = "SH-ENGL 4"  # English 4
v = "ENTREP"  # Entrepreneurship
w = "SH-HS 3"  # Hardware and Servicing 3
x = "SH-PE 3"  # Physical Education 3
y = "SH-RES 2"  # Research 2
z = "SH-SOCSCI 2"  # Social Science 2

# Year 12 Second Semester Subject Codes
aa = "SH-CP 4"  # Computer Programming 4
ab = "SH-3I"  # Inquiries, Investigations, and Immersion (research project culminating activity)
ac = "SH-ENGL 5"  # English 5
ad = "SH-FIL 3"  # Filipino 3
ae = "SH-HS 4"  # Hardware and Servicing 4
af = "SH-PE 4"  # Physical Education 4
ag = "SH-OJT/ICT"  # On-the-Job Training / Information and Communications Technology
ah = "SH-PE 4"  # Physical Education 4
ai = "SH-PHYSCI 1"  # Physical Science 1


def main_dashboard():
    # Function to display the main dashboard of the application
    print("")  # Print a blank line for spacing
    print("***MAIN DASHBOARD***")  # Title of the main dashboard
    print("-------------------------------------------")  # Divider line for visual separation
    print("1. Login (Admin)")  # Option for admin login
    print("2. Login (Student)")  # Option for student login
    print("3. Login (Teacher)")  # Option for teacher login
    print("4. Exit")  # Option to exit the application
    print("-------------------------------------------")  # Another divider line for visual separation

    while True:  # Infinite loop to keep the dashboard running until exit is selected
        choose = str(input("Enter an option: ")).strip()  # Prompting the user for their choice, strip to remove extra spaces

        if choose == "1":  # If the user chooses admin login
            while True:  # Infinite loop for admin login
                username = input("Enter username: ").strip()  # Prompt for admin username, strip removes extra spaces
                admins = admin_in_db.find_one({"Username": username})  # Check if the username exists in the admin collection
                if admins:  # If username is found
                    while True:  # Infinite loop for password entry
                        password = input("Enter password: ").strip()  # Prompt for admin password
                        find_pass = admin_in_db.find_one({"Username": username, "Password": password})  # Check if username-password pair is correct
                        if find_pass:  # If the username-password combination is correct
                            admin_dashboard()  # Call the admin dashboard function for a successful login
                            break  # Exit the password loop and return to the main dashboard after successful login
                        else:
                            print("Password incorrect. Please try again.")  # Inform the user if the password is incorrect
                else:
                    print("Username incorrect. Please try again.")  # Inform the user if the username is not found in the database

        elif choose == "2":  # If the user chooses student login
            login_student()  # Call the student login function
            break  # Exit the main dashboard loop after student login is initiated

        elif choose == "3":  # If the user chooses teacher login
            login_sub_teacher()  # Call the teacher login function
            break  # Exit the main dashboard loop after teacher login is initiated

        elif choose == "4":  # If the user chooses to exit
            raise SystemExit  # Exit the program immediately

        else:  # If the user enters an invalid option
            print("Option does not exist. Please try again")  # Inform the user that their choice is invalid


def admin_dashboard():
    # Function to display the admin dashboard of the application
    print("")  # Print a blank line for spacing
    print("------------------------------------------------------------")  # Divider line
    print("  Welcome to TVL-ICT Senior High Student Management System  ")  # Welcome message for the admin
    print("------------------------------------------------------------")  # Divider line
    print("")  # Print a blank line for spacing

    # Displaying the options available in the admin dashboard
    print("1. Enroll Regular Student")  # Option to enroll a regular student
    print("2. Enroll Irregular Student")  # Option to enroll an irregular student
    print("3. Update Student Final Grade")  # Option to update a student's final grade
    print("4. Update Student")  # Option to update student information (e.g., details like name, age, etc.)
    print("5. Delete Student")  # Option to delete a student record
    print("6. Add Subject Teacher") # Option to add a subject teacher to the system
    print("7. Logout")  # Option for the admin to log out and return to the main dashboard
    print("")  # Print a blank line for spacing

    while True:  # Infinite loop to keep the admin dashboard running until the admin logs out
        choose = input("Enter an option: ").strip()  # Prompt the admin to choose an option by entering a number

        if choose == "1": # If the admin chooses to enroll a regular student
            while True:
                opt = input("Do you want to enroll a student? (yes or no): ").lower().strip()
                if opt == "yes":
                    enroll_student() # Call the function to handle regular student enrollment
                elif opt == "no":
                    admin_dashboard()
                else:
                    print("Please follow the sample")

        elif choose == "2": # If the admin chooses to enroll an irregular student
            while True:
                opt = input("Do you want to enroll a student? (yes or no): ").lower().strip()
                if opt == "yes":
                    enroll_irregular_student() # Call the function to handle irregular student enrollment
                    break
                elif opt == "no":
                    admin_dashboard()
                    break
                else:
                    print("Please follow the sample")

        elif choose == "3":  # Option to update student grades (this section could be expanded later)
            update_student_final_grade()  # Call the function to update the student's final grade (functionality may be defined elsewhere)
        elif choose == "4":  # Option to update student details (name, age, etc.)
            update_student()  # Call the function to update student information (the function could involve editing student details)
        elif choose == "5":  # Option to delete a student record
            delete_student()  # Call the function to delete a student's record from the database
        elif choose == "6":  # If the admin chooses to add a subject teacher
            add_sub_teacher()  # Call the function to add a subject teacher to the database
        elif choose == "7":
            main_dashboard() #calls out the main dashboard function if the admin wants to logout
        else:  # If the admin enters an invalid option
            print("Option does not exist. Please try again.")  # Inform the admin that the option is invalid


def delete_student():
    # Retrieving all students from both regular and irregular enrollment collections
    all_students = students_enrolled.find()  # Get all regular students
    all_students2 = irregular_student_enrolled.find()  # Get all irregular students
    count_student = students_enrolled.count_documents({})  # Count the number of regular students enrolled
    count_student_irreg = irregular_student_enrolled.count_documents({})  # Count the number of irregular students enrolled

    # Displaying options for the admin to choose from
    print("1. Delete Regular Student")  # Option to delete a regular student
    print("2. Delete Irregular Student")  # Option to delete an irregular student
    print("3. Exit")  # Option to exit the delete function and return to the admin dashboard
    print("")  # Print a blank line for spacing
    while True:
        choose = input("Enter an option: ").strip() # Prompt for the admin's choice (1, 2, or 3)

        if choose == "1":  # If the admin chooses to delete a regular student
            if count_student == 0:  # Check if there are no regular students enrolled
                print("No regular student enrolled.")  # Inform the admin if no regular students are available to delete
            else:
                num = 0  # Initialize a counter for listing students
                print("Eligible Students for Deletion")  # Inform the admin about students available for deletion
                print("--------------------------------------------------")
                for student in all_students:  # Loop through all regular students
                    num += 1  # Increment the student counter
                    # Print the student's first name, last name, and ID for reference
                    print(f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
                print("--------------------------------------------------")  # Divider line for clarity
                print("")  # Print a blank line for spacing

                # Loop to allow the admin to find a student by first name
                while True:
                    find_fn = input("Enter student's first name: ").upper()  # Prompt for first name, convert to uppercase for uniformity
                    if students_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists in the regular students collection
                        # If the first name is found, prompt for last name
                        while True:
                            find_ln = input("Enter student's last name: ").upper()  # Prompt for last name, convert to uppercase
                            if students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln}):  # Check if both first and last name match
                                # If both names are found, prompt for the student ID
                                while True:
                                    find_id = input("Enter student's ID: ")  # Prompt for student ID
                                    if students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id}):  # Check if the ID matches
                                        delete_regular_student(find_fn, find_ln, find_id)  # Call the function to delete the regular student
                                        return find_fn, find_ln, find_id  # Return the student's name and ID after deletion
                                    else:
                                        print("Incorrect student ID. Please try again.")  # Inform the admin if the ID is incorrect
                            else:
                                print("Student's last name does not exist. Kindly re-enter the information.")  # Inform the admin if the last name does not match
                    else:
                        print("Student does not exist. Please try again.")  # Inform the admin if the first name doesn't exist in the database

        elif choose == "2":  # If the admin chooses to delete an irregular student
            if count_student_irreg == 0:  # Check if there are no irregular students enrolled
                print("No irregular student enrolled.")  # Inform the admin if no irregular students are available to delete
            else:
                num = 0  # Initialize a counter for listing students
                print("Eligible Students for Deletion")  # Inform the admin about students available for deletion
                print("--------------------------------------------------")
                for student in all_students2:  # Loop through all irregular students
                    num += 1  # Increment the student counter
                    # Print the student's first name, last name, and ID for reference
                    print(f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
                print("--------------------------------------------------")  # Divider line for clarity
                print("")  # Print a blank line for spacing

                # Loop to allow the admin to find a student by first name
                while True:
                    find_fn = input("Enter student's first name: ").upper()  # Prompt for first name, convert to uppercase
                    if irregular_student_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists in the irregular students collection
                        # If the first name is found, prompt for last name
                        while True:
                            find_ln = input("Enter student's last name: ").upper()  # Prompt for last name, convert to uppercase
                            if irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln}):  # Check if both first and last name match
                                # If both names are found, prompt for the student ID
                                while True:
                                    find_id = input("Enter student's ID: ")  # Prompt for student ID
                                    if irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id}):  # Check if the ID matches
                                        delete_irreg_student(find_fn, find_ln, find_id)  # Call the function to delete the irregular student
                                        return find_fn, find_ln, find_id  # Return the student's name and ID after deletion
                                    else:
                                        print("Incorrect student ID. Please try again.")  # Inform the admin if the ID is incorrect
                            else:
                                print("Student's last name does not exist. Kindly re-enter the information.")  # Inform the admin if the last name does not match
                    else:
                        print("Student does not exist. Please try again. ")  # Inform the admin if the first name doesn't exist in the database

        elif choose == "3":  # If the admin chooses to exit the deletion process
            admin_dashboard()  # Return to the admin dashboard

        else:  # If the admin enters an invalid option
            print("Option does not exist. Please try again.")  # Inform the admin that the entered option is invalid

def update_student():
    # Retrieve all students from both regular and irregular enrollment collections
    all_students = students_enrolled.find()  # Fetch regular students
    all_students2 = irregular_student_enrolled.find()  # Fetch irregular students
    count_student = students_enrolled.count_documents({})  # Count regular students
    count_student_irreg = irregular_student_enrolled.count_documents({})  # Count irregular students

    # Present options for updating a student
    print("1. Update Regular Student")  # Option to update a regular student
    print("2. Update Irregular Student")  # Option to update an irregular student
    print("3. Exit")  # Option to exit and return to the admin dashboard

    print("")  # Print a blank line for spacing
    choose = input("Enter an option: ").strip()  # Prompt the admin for their choice (1, 2, or 3)

    if choose == "1":  # If the admin chooses to update a regular student
        if count_student == 0:  # Check if no regular students are enrolled
            print("--------------------------------------------------------------")
            print("No regular student has been enrolled, please enroll a student.")  # Inform the admin that there are no regular students
            print("--------------------------------------------------------------")
            admin_dashboard()  # Return to the admin dashboard if no students are enrolled

        else:
            num = 0  # Initialize a counter for listing students
            print("Students Eligible for Update")  # Inform the admin about the students available for update
            print("--------------------------------------------------")
            for student in all_students:  # Loop through all regular students
                num += 1  # Increment the counter
                # Display the student's first name, last name, and ID for reference
                print(f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
            print("--------------------------------------------------")  # Divider line for clarity
            print("")  # Print a blank line for spacing

            # Loop to allow the admin to search for the student by their first name
            while True:
                find_fn = input("Enter student's first name: ").upper()  # Prompt for first name, convert to uppercase
                if students_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists
                    # If the first name is found, prompt for last name
                    while True:
                        find_ln = input("Enter student's last name: ").upper()  # Prompt for last name, convert to uppercase
                        if students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln}):  # Check if both first and last name match
                            # If both names are found, prompt for the student ID
                            while True:
                                find_id = input("Enter student's ID: ")  # Prompt for student ID
                                if students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id}):  # Check if the ID matches
                                    update_regular_student(find_fn, find_ln, find_id)  # Call the function to update the regular student
                                    return find_fn, find_ln, find_id  # Return the student's name and ID after the update
                                else:
                                    print("Incorrect Student ID. Please try again.")  # Inform the admin if the ID is incorrect
                        else:
                            print("Student's last name does not exist. Please try again.")  # Inform the admin if the last name does not exist
                else:
                    print("Student does not exist. Please try again.")  # Inform the admin if the first name doesn't exist in the database

    elif choose == "2":  # If the admin chooses to update an irregular student
        if count_student_irreg == 0:  # Check if no irregular students are enrolled
            print("----------------------------------------------------------------")
            print("No irregular student has been enrolled, please enroll a student.")  # Inform the admin if no irregular students are available
            print("----------------------------------------------------------------")
            admin_dashboard()  # Return to the admin dashboard if no irregular students

        else:
            num = 0  # Initialize a counter for listing students
            print("Students Eligible for Update")  # Inform the admin about the students available for update
            print("--------------------------------------------------")
            for student in all_students2:  # Loop through all irregular students
                num += 1  # Increment the counter
                # Display the student's first name, last name, and ID for reference
                print(f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
            print("--------------------------------------------------")  # Divider line for clarity
            print("")  # Print a blank line for spacing

            # Loop to allow the admin to search for the student by their first name
            while True:
                find_fn = input("Enter student's first Name: ").upper()  # Prompt for first name, convert to uppercase
                if irregular_student_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists
                    # If the first name is found, prompt for last name
                    while True:
                        find_ln = input("Enter student's last Name: ").upper()  # Prompt for last name, convert to uppercase
                        if irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln}):  # Check if both first and last name match
                            # If both names are found, prompt for the student ID
                            while True:
                                find_id = input("Enter student's ID: ")  # Prompt for student ID
                                if irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id}):  # Check if the ID matches
                                    update_irreg_student(find_fn, find_ln, find_id)  # Call the function to update the irregular student
                                    return find_fn, find_ln, find_id  # Return the student's name and ID after the update
                                else:
                                    print("Incorrect student ID. Please try again.")  # Inform the admin if the ID is incorrect
                        else:
                            print("Students last name does not exist. Please try again.")  # Inform the admin if the last name does not exist
                else:
                    print("Student does not exist. Please try again.")  # Inform the admin if the first name doesn't exist in the database

    elif choose == "3":  # If the admin chooses to exit
        admin_dashboard()  # Return to the admin dashboard

    else:  # If the admin enters an invalid option
        print("Option does not exist. Please try again.")  # Inform the admin that the entered option is invalid

def update_student_final_grade():
    # Retrieve all students from both regular and irregular enrollment collections
    all_students = students_enrolled.find()  # Fetch regular students
    list_all_students = list(all_students)  # Convert document to a list of regular students

    all_students2 = irregular_student_enrolled.find()  # Fetch irregular students
    list_all_students2 = list(all_students2)  # Convert document to a list of irregular students

    count_student = students_enrolled.count_documents({})  # Count regular students
    count_student_irreg = irregular_student_enrolled.count_documents({})  # Count irregular students

    # Present options for updating final grades
    print("1. Update Regular Student (Final Grade)")  # Option to update final grade of a regular student
    print("2. Update Irregular Student (Final Grade)")  # Option to update final grade of an irregular student
    print("3. Exit")  # Option to exit and return to the admin dashboard

    print("")  # Print a blank line for spacing
    while True:
        choose = input("Enter an option: ").strip()  # Prompt for admin choice (1, 2, or 3)

        if choose == "1":  # If the admin chooses to update the final grade of a regular student
            if count_student == 0:  # Check if there are no regular students enrolled
                print("--------------------------------------------------------------")
                print("No regular student has been enrolled, please enroll a student.")  # Inform the admin
                print("--------------------------------------------------------------")
                admin_dashboard()  # Return to the admin dashboard if no students are enrolled
            else:
                num = 0  # Initialize a counter for listing students
                print("List of Students:")  # Inform the admin about the available students
                print("---------------------------------")
                for student in list_all_students:  # Loop through all regular students
                    num += 1  # Increment the counter
                    # Display the student's first name, last name, and ID for reference
                    print(
                        f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
                print("---------------------------------")
                print("")  # Print a blank line for spacing

                # Loop to allow the admin to search for the student by first name, last name, and ID
                while True:
                    find_fn = input(
                        "Enter student's first name: ").upper().strip()  # Prompt for first name, convert to uppercase
                    if students_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists
                        while True:
                            find_ln = input("Enter student's last name: ").upper().strip()  # Prompt for last name, convert to uppercase
                            if students_enrolled.find_one({"FirstName": find_fn,
                                                           "LastName": find_ln}):  # Check if both first and last names match
                                while True:
                                    find_id = input("Enter student's ID: ").strip()  # Prompt for student ID
                                    student_record = students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})
                                    if student_record: # If the student record is found

                                        student = students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})
                                        indexs = 0
                                        print("Student's Subjects and Grades")
                                        print("------------------------------------------------")
                                        for subjects, grades in student['Subjects'].items():
                                            indexs += 1
                                            print(f'{indexs}. Subject: {subjects} | Grades: {grades}')
                                        print("------------------------------------------------")
                                        print("")

                                        while True:
                                            option = input("Do you want to update Final Grade of Student? (yes or no): ").lower().strip()
                                            if option == "yes":
                                                update_final_grade_of_student(find_fn, find_ln,find_id)  # Call function to update final grade
                                                return find_fn, find_ln, find_id  # Return the student's name and ID after the update
                                            elif option == "no":
                                                update_student_final_grade()
                                            else:
                                                print("Please follow the guide")

                                    else:
                                        print(
                                            "Incorrect student ID. Please try again.")  # Inform the admin if the ID is incorrect
                            else:
                                print(
                                    "Student's last name does not exist. Please try again.")  # Inform the admin if the last name is incorrect
                    else:
                        print(
                            "Student does not exist. Kindly re-enter the information.")  # Inform the admin if the first name doesn't exist in the database

        elif choose == "2":  # If the admin chooses to update the final grade of an irregular student
            if count_student_irreg == 0:  # Check if there are no irregular students enrolled
                print("----------------------------------------------------------------")
                print("No irregular student has been enrolled, please enroll a student.")  # Inform the admin
                print("----------------------------------------------------------------")
                admin_dashboard()  # Return to the admin dashboard if no irregular students are enrolled
            else:
                num = 0  # Initialize a counter for listing students
                print("Students Eligible for Update")  # Inform the admin about the available students
                print("--------------------------------------------------")
                for student in list_all_students2:  # Loop through all irregular students
                    num += 1  # Increment the counter
                    # Display the student's first name, last name, and ID for reference
                    print(
                        f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
                print("--------------------------------------------------")
                print("")  # Print a blank line for spacing

                # Loop to allow the admin to search for the student by first name, last name, and ID
                while True:
                    find_fn = input("Enter student's first name: ").upper().strip()  # Prompt for first name, convert to uppercase
                    if irregular_student_enrolled.find_one({"FirstName": find_fn}):  # Check if the first name exists
                        while True:
                            find_ln = input(
                                "Enter student's last name: ").upper().strip()  # Prompt for last name, convert to uppercase
                            if irregular_student_enrolled.find_one({"FirstName": find_fn,
                                                                    "LastName": find_ln}):  # Check if both first and last names match
                                while True:
                                    find_id = input("Enter student's ID: ").strip()  # Prompt for student ID
                                    student_record = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

                                    if student_record:  # If the student record is found

                                        student = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})
                                        indexs = 0
                                        print("Student's Subjects and Grades")
                                        print("------------------------------------------------")
                                        for subjects, grades in student['Subjects'].items():
                                            indexs += 1
                                            print(f'{indexs}. Subject: {subjects} | Grades: {grades}')
                                        print("------------------------------------------------")
                                        print("")

                                        while True:
                                            option = input("Do you want to update Final Grade of Student? (yes or no): ").lower().strip()
                                            if option == "yes":
                                                update_final_grade_of_irregular(find_fn, find_ln,find_id)  # Call function to update final grade
                                                return find_fn, find_ln, find_id  # Return the student's name and ID after the update
                                            elif option == "no":
                                                update_student_final_grade()
                                            else:
                                                print("Please follow the guide") # Return the student's name and ID after the update
                                    else:
                                        print(
                                            "Incorrect Student ID. Please try again.")  # Inform the admin if the ID is incorrect
                            else:
                                print(
                                    "Student's Last Name does not exist. Please try again.")  # Inform the admin if the last name is incorrect
                    else:
                        print(
                            "Student does not exist. Kindly re-enter the information.")  # Inform the admin if the first name doesn't exist in the database

        elif choose == "3":  # If the admin chooses to exit
            admin_dashboard()  # Return to the admin dashboard

        else:  # If the admin enters an invalid option
            print("Option does not exist. Please try again.")  # Inform the admin that the entered option is invalid


def delete_regular_student(find_fn, find_ln, find_id):
    # Inform the user that the deletion process is starting
    print("Deleting Student Record...")
    print("")

    # Search for the student using the first name, last name, and student ID
    find_student = students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # Check if the student exists in the database
    if not find_student:
        print("Student not found. Please ensure the identification details are correct.")
        return  # If the student is not found, exit the function

    # If the student is found, proceed with deletion
    for old_subject, grades in find_student["Subjects"].items():  # Loop through each subject the student is enrolled in
        # Check if the subject has a teacher assigned in the teacher database
        find_old_sub_teacher = sub_teacher_in_db.find({"Subject To Handle": old_subject})
        if find_old_sub_teacher:  # If the subject has a teacher
            old_student_info = {"ID": find_student.get("ID"), "FirstName": find_fn, "LastName": find_ln}
            # Remove the student from the subject's list of students handled by the teacher
            sub_teacher_in_db.update_one(
                {"Subject To Handle": old_subject},
                {"$pull": {"Students": old_student_info}})

    # Delete the student from the main student database (students_enrolled)
    students_enrolled.delete_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # Inform the admin that the student has been successfully deleted
    print(f'{find_id}, has been deleted.')
    print("")
    print("--------------------------------------------------")

    # List all remaining students after the deletion
    num = 0
    for student in students_enrolled.find():  # Fetch all remaining students
        num += 1  # Increment counter for each student
        print(
            f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
    print("--------------------------------------------------")

    # Ask the admin if they want to delete another student
    while True:
        choose = input("Do you want to delete another student? (yes or no) : ").lower().strip()
        if choose == "yes":  # If the admin says yes, call delete_student() to continue deletion process
            delete_student()
        elif choose == "no":  # If the admin says no, return to the admin dashboard
            admin_dashboard()
        else:  # If the admin provides an invalid response, prompt them again
            print("Invalid input. Please enter 'yes' or 'no'.")

def delete_irreg_student(find_fn, find_ln, find_id):
    # Inform the user that the deletion process is starting
    print("Deleting Student Record...")
    print("")

    # Search for the irregular student using the first name, last name, and student ID
    find_student = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # Check if the student exists in the database
    if not find_student:
        print("Student not found. Please ensure the identification details are correct.")
        return  # If the student is not found, exit the function

    # If the student is found, proceed with deletion
    for old_subject, grades in find_student["Subjects"].items():  # Loop through each subject the student is enrolled in
        # Check if the subject has a teacher assigned in the teacher database
        find_old_sub_teacher = sub_teacher_in_db.find({"Subject To Handle": old_subject})
        if find_old_sub_teacher:  # If the subject has a teacher
            old_student_info = {"ID": find_student.get("ID"), "FirstName": find_fn, "LastName": find_ln}
            # Remove the student from the subject's list of students handled by the teacher
            sub_teacher_in_db.update_one(
                {"Subject To Handle": old_subject},
                {"$pull": {"Students": old_student_info}})

    # Delete the student from the irregular student database (irregular_student_enrolled)
    irregular_student_enrolled.delete_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # Inform the admin that the student has been successfully deleted
    print(f'{find_id}, has been deleted.')
    print("")
    print("------------------------------------------------")

    # List all remaining irregular students after the deletion
    num = 0
    for student in irregular_student_enrolled.find():  # Fetch all remaining students
        num += 1  # Increment counter for each student
        print(
            f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
    print("------------------------------------------------")

    # Ask the admin if they want to delete another student
    while True:
        choose = input("Do you want to delete another student? (yes/no) : ").lower().strip()
        if choose == "yes":  # If the admin says yes, call delete_student() to continue deletion process
            delete_student()
        elif choose == "no":  # If the admin says no, return to the admin dashboard
            admin_dashboard()
        else:  # If the admin provides an invalid response, prompt them again
            print("Invalid input. Please enter 'yes' or 'no'.")



def update_final_grade_of_student(find_fn, find_ln, find_id):
    # Search for the student in the enrolled students database using first name, last name, and student ID
    find_student = students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # If the student is not found, print an error message and return
    if find_student is None:
        print("Student not found.")
        return None  # or handle this case as needed

    # Proceed to calculate average grade if student is found
    subjects = find_student.get('Subjects', {})  # Get the student's subjects (a dictionary of subjects and grades)

    # If the student has no subjects, print an error and return
    if not subjects:  # Check if Subjects is empty
        print("No subjects found for this student.")
        return None

    # Sum all the grades for the student
    total_grades = sum(subjects.values())  # Sum of all grades in subjects
    num_of_sub = len(subjects)  # Get the number of subjects the student is enrolled in

    # If the student has subjects, calculate the average grade
    if num_of_sub > 0:  # Avoid division by zero
        average_grade = total_grades / num_of_sub  # Calculate the average grade
        # Update the student's final grade in the database
        students_enrolled.update_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id}, {"$set": {"Final Grade": average_grade}})
    else:
        print("No subjects found.")
        return None  # Handle case where no subjects exist for the student

    # Inform the admin that the student's final grade has been updated
    get_student = students_enrolled.find_one(
        {"FirstName": find_fn, "LastName": find_ln, "ID": find_id, "Final Grade": average_grade})
    print("---------------------------------------")
    print(
        f'First Name: {get_student.get("FirstName")} | Last Name: {get_student.get("LastName")} | ID: {get_student.get("ID")} | Final Grade: {get_student.get("Final Grade")}')
    print("---------------------------------------")
    print("")
    print(f"{find_id}, final grade has been updated")

    # Prompt the admin if they want to update another student's final grade
    while True:
        choose = input("Do you want to update another students final grade? (yes or no) : ").lower().strip()
        if choose == "yes":  # If yes, recursively call the function to update another student's grade
            update_student_final_grade()
        elif choose == "no":  # If no, return to the admin dashboard
            admin_dashboard()
        else:  # If the input is not 'yes' or 'no', prompt again
            print("Invalid input. Please enter 'yes' or 'no'.")


def update_final_grade_of_irregular(find_fn, find_ln, find_id):
    # Search for the irregular student in the enrolled students database using first name, last name, and student ID
    find_student = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # If the student is not found, print an error message and return
    if find_student is None:
        print("Student not found. Kindly re-enter the information.")
        return None  # or handle this case as needed

    # Proceed to calculate average grade if student is found
    subjects = find_student.get('Subjects', {})  # Get the student's subjects (a dictionary of subjects and grades)

    # If the student has no subjects, print an error and return
    if not subjects:  # Check if Subjects is empty
        print("No subjects found for this student.")
        return None

    # Sum all the grades for the student
    total_grades = sum(subjects.values())  # Sum of all grades in subjects
    num_of_sub = len(subjects)  # Get the number of subjects the student is enrolled in

    # If the student has subjects, calculate the average grade
    if num_of_sub > 0:  # Avoid division by zero
        average_grade = total_grades / num_of_sub  # Calculate the average grade
        # Update the student's final grade in the database
        irregular_student_enrolled.update_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id},
                                     {"$set": {"Final Grade": average_grade}})

    else:
        print("No subjects found.")
        return None  # Handle case where no subjects exist for the student

    # Inform the admin that the student's final grade has been updated
    get_student = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id, "Final Grade": average_grade})
    print("---------------------------------------")
    print(f'First Name: {get_student.get("FirstName")} | Last Name: {get_student.get("LastName")} | ID: {get_student.get("ID")} | Final Grade: {get_student.get("Final Grade")}')
    print("---------------------------------------")
    print("")
    print(f"{find_id}, final grade has been updated")

    # Prompt the admin if they want to update another student's final grade
    while True:
        choose = input("Do you want to update another students final grade? (yes or no) : ").lower().strip()
        if choose == "yes":  # If yes, recursively call the function to update another student's grade
            update_student_final_grade()
        elif choose == "no":  # If no, return to the admin dashboard
            admin_dashboard()
        else:  # If the input is not 'yes' or 'no', prompt again
            print("Invalid input. Please enter 'yes' or 'no'.")


def update_regular_student(find_fn, find_ln, find_id):
    # Print the update section header
    print("UPDATE SECTION")
    print("")

    # Search for the student in the database by first name, last name, and ID
    find_student = students_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    # If the student is not found, print an error message and return
    if not find_student:
        print("Student not found. Please ensure the identification details are correct.")
        return  # Exit the function early if the student is not found

    # Proceed only if find_student is valid
    for old_subject, grades in find_student["Subjects"].items():
        # Find the teacher assigned to the old subject and remove the student from their list
        find_old_sub_teacher = sub_teacher_in_db.find({"Subject To Handle": old_subject})
        if find_old_sub_teacher:
            old_student_info = {"ID": find_student.get("ID"), "FirstName": find_fn, "LastName": find_ln}
            sub_teacher_in_db.update_one(
                {"Subject To Handle": old_subject},
                {"$pull": {"Students": old_student_info}})

    # If the student is found, proceed with the update
    if find_student:
        print(f'Update Student | Name: {find_student.get("FirstName")} {find_student.get("LastName")} | ID: {find_student.get("ID")}')
        print("-----------------------------------------")

        # Prompt for new student details such as name, birthdate, year level, and semester
        new_fn = input("Enter student's first name: ").upper()  # First name input
        new_mn = input("Enter student's middle name: ").upper()  # Middle name input
        new_ln = input("Enter student's last name: ").upper()  # Last name input

        # Infinite loop to gather birth date input with validation
        while True:
            new_bday = input("Enter birth date (MM/DD/YY): ").strip()  # Prompt for birth date
            upper = re.search(r'[A-Z]', new_bday)  # Check for uppercase letters
            lower = re.search(r'[a-z]', new_bday)  # Check for lowercase letters
            if len(new_bday) >= 11:  # If the birth date is too long
                print("Invalid birth date. Please try again.")
            else:
                # Validate that the birth date contains only digits (no letters)
                if upper:  # If it contains uppercase letters
                    print("Only digits will be accepted. Please try again.")
                elif lower:  # If it contains lowercase letters
                    print("Only digits will be accepted. Please try again.")
                else:
                    while True:
                        new_year_lvl = input("Enter student year level (11 or 12): ").strip()  # Prompt for year level
                        if new_year_lvl == "11":
                            # Handle the first semester of year 11
                            while True:
                                new_sem = input("Enter semester (1st or 2nd): ").upper().strip()  # Prompt for semester
                                if new_sem == "1ST":
                                    num = 0  # Counter for subjects
                                    print("Subjects to take:")  # List subjects for the first semester of year 11
                                    print("-------------------------")
                                    for subs in (a, b, c, d, e, f, g, h, i):
                                        num += 1
                                        print(f'{num}. {subs}')  # Print each subject
                                    print("-------------------------")

                                    # Update the student's information in the database
                                    students_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                 {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_student.get("ID"),
                                                                           "Subjects": {a: 0, b: 0, c: 0, d: 0, e: 0, f: 0, g: 0, h: 0, i: 0},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade,
                                                                           "StudentStatus": "Regular Student"}})

                                    # Add the student to the teacher's list for each subject
                                    for sub_teacher in [a, b, c, d, e, f, g, h, i]:
                                        find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                        if find_sub_teacher > 0:
                                            new_student_info = {"ID": find_student.get("ID"), "FirstName": new_fn, "LastName": new_ln}
                                            sub_teacher_in_db.update_one(
                                                {"Subject To Handle": sub_teacher},
                                                {"$push": {"Students": new_student_info}})
                                        else:
                                            print(f'No teacher has been assigned to {sub_teacher} yet.')
                                    break
                                elif new_sem == "2ND":
                                    # Handle the second semester of year 11 in a similar way
                                    num = 0
                                    print("Subjects to take:")
                                    print("-------------------------")
                                    for subs in (j, k, l, m, n, o, p, q, r):
                                        num += 1
                                        print(f'{num}. {subs}')
                                    print("-------------------------")

                                    # Update the student's information for the second semester
                                    students_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                 {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_student.get("ID"),
                                                                           "Subjects": {j: 0, k: 0, l: 0, m: 0, n: 0, o: 0, p: 0, q: 0, r: 0},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade,
                                                                           "StudentStatus": "Regular Student"}})

                                    # Add the student to each subject's teacher list
                                    for sub_teacher in [j, k, l, m, n, o, p, q, r]:
                                        find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                        if find_sub_teacher > 0:
                                            new_student_info = {"ID": find_student.get("ID"), "FirstName": new_fn, "LastName": new_ln}
                                            sub_teacher_in_db.update_one(
                                                {"Subject To Handle": sub_teacher},
                                                {"$push": {"Students": new_student_info}})
                                        else:
                                            print(f'No teacher has been assigned to {sub_teacher} yet.')
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                            break

                        # Similar handling for year level 12
                        elif new_year_lvl == "12":
                            while True:
                                new_sem = input("Enter Semester (1st/2nd): ").upper().strip()  # Prompt for semester
                                if new_sem == "1ST":
                                    num = 0
                                    print("Subjects to take:")
                                    for subs in (s, t, u, v, w, x, y, z):
                                        num += 1
                                        print(f'{num}. {subs}')
                                    print("-------------------------")

                                    # Update the student's information for year 12, first semester
                                    students_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                 {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_student.get("ID"),
                                                                           "Subjects": {s: 0, t: 0, u: 0, v: 0, w: 0, x: 0, y: 0, z: 0},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade,
                                                                           "StudentStatus": "Regular Student"}})

                                    for sub_teacher in [s, t, u, v, w, x, y, z]:
                                        find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                        if find_sub_teacher > 0:
                                            new_student_info = {"ID": find_student.get("ID"), "FirstName": new_fn, "LastName": new_ln}
                                            sub_teacher_in_db.update_one(
                                                {"Subject To Handle": sub_teacher},
                                                {"$push": {"Students": new_student_info}})
                                        else:
                                            print(f'No teacher has been assigned to {sub_teacher} yet')
                                    break
                                elif new_sem == "2ND":
                                    num = 0
                                    print("Subjects to take:")
                                    for subs in (aa, ab, ac, ad, ae, af, ag, ah, ai):
                                        num += 1
                                        print(f'{num}. {subs}')
                                    print("-------------------------")

                                    # Update the student's information for year 12, second semester
                                    students_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                 {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_student.get("ID"),
                                                                           "Subjects": {aa: 0, ab: 0, ac: 0, ad: 0, ae: 0, af: 0, ag: 0, ah: 0, ai: 0},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade,
                                                                           "StudentStatus": "Regular Student"}})

                                    for sub_teacher in [aa, ab, ac, ad, ae, af, ag, ah, ai]:
                                        find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                        if find_sub_teacher > 0:
                                            new_student_info = {"ID": find_student.get("ID"), "FirstName": new_fn, "LastName": new_ln}
                                            sub_teacher_in_db.update_one(
                                                {"Subject To Handle": sub_teacher},
                                                {"$push": {"Students": new_student_info}})
                                        else:
                                            print(f'No teacher has been assigned to {sub_teacher} yet')
                                    break
                                else:
                                    print("Invalid input. Please try again.")
                            break
                        else:
                            print("Please enter a valid year level: '11' or '12'.")

                print("---------------------------")
                print(" UPDATE ACCOUNT OF STUDENT ")
                print("---------------------------")

                # Check if the student exists before proceeding with account update
                find_student_to_upd_account = students_enrolled.find_one(
                    {"FirstName": new_fn, "LastName": new_ln, "ID": find_id})

                if find_student_to_upd_account:  # If the student exists
                    while True:  # Infinite loop for username input
                        new_username = input(
                            "Please enter a username (must be at least 8 characters): ").upper().strip()  # Prompt for username
                        if len(new_username) <= 7:  # Check username length
                            print("Username must be at least 8 characters long.")  # Inform user of error
                        else:
                            while True:  # Infinite loop for password input
                                new_password = input("Please enter a password (must be at least 6 characters long, include an uppercase letter, a lowercase letter, and a digit): ").strip()  # Prompt for password
                                # Check if password exists in any collection
                                find_password = (((students_enrolled.find_one({"Password": new_password}) or
                                                   irregular_student_enrolled.find_one(
                                                       {"Password": new_password})) or
                                                  teacher_in_db.find_one({"Password": new_password})) or
                                                 sub_teacher_in_db.find_one({"Password": new_password}))

                                if len(new_password) <= 5:  # Check password length
                                    print("Password be at least 6 characters long.")  # Inform user of error
                                elif find_password:  # If password already exists
                                    print("Password already exists. Please try again.")  # Inform user of error
                                else:
                                    # Check password criteria
                                    upper = re.search(r'[A-Z]', new_password)  # Check for uppercase letters
                                    lower = re.search(r'[a-z]', new_password)  # Check for lowercase letters
                                    numbers = re.search(r'[0-9]', new_password)  # Check for digits

                                    if not upper:  # If no uppercase letters
                                        print("Password must include an uppercase letter. Please try again.")
                                    elif not lower:  # If no lowercase letters
                                        print("Password must include a lowercase letter. Please try again.")
                                    else:
                                        if not numbers:
                                            print("Password must include digits. PLease try again")
                                        else:
                                            # Update the student's username and password in the database
                                            students_enrolled.update_one(
                                                {"FirstName": new_fn, "ID": find_id},
                                                {"$set": {"Username": new_username, "Password": new_password}})
                                            print(f"Student ID: {find_id}, has been updated")  # Confirmation message
                                            print("")  # Print a blank line for spacing
                                            print("")  # Print a blank line for spacing
                                            print("")  # Print a blank line for spacing

                                            while True:  # Infinite loop for enrollment option
                                                opt = input(
                                                    "Do you want to update another student? (yes or no): ").lower().strip()  # Prompt for another enrollment
                                                if opt == "yes":  # If user wants to enroll another student
                                                    update_student()  # Recursive call to enroll another student
                                                    break  # Exit loop
                                                elif opt == "no":  # If user does not want to enroll another student
                                                    admin_dashboard()  # Redirect to admin dashboard
                                                    break  # Exit loop
                                                else:
                                                    print(
                                                        "Invalid input. Please enter 'yes' or 'no'.")  # Inform user of incorrect input
                                        break  # Exit password input loop
                            break  # Exit username input loop
                else:
                    print("Student not found. Kindly re-enter the information.")

def update_irreg_student(find_fn, find_ln, find_id):
    print("UPDATE SECTION")
    print("")
    find_student = irregular_student_enrolled.find_one({"FirstName": find_fn, "LastName": find_ln, "ID": find_id})

    for old_subject, grades in find_student["Subjects"].items():
        find_old_sub_teacher = sub_teacher_in_db.find({"Subject To Handle": old_subject})
        if find_old_sub_teacher:
            old_student_info = {"ID": find_student.get("ID"), "FirstName": find_fn,
                                "LastName": find_ln}
            sub_teacher_in_db.update_one(
                {"Subject To Handle": old_subject},
                {"$pull": {"Students": old_student_info}})

    if find_student:
        print(f'Update Student | Name: {find_student.get("FirstName")} {find_student.get("LastName")} | ID: {find_student.get("ID")}')
        print("-----------------------------------------")

        new_fn = input("Enter student's first name: ").upper()  # First name input
        new_mn = input("Enter student's middle name: ").upper()  # Middle name input
        new_ln = input("Enter student's last name: ").upper()  # Last name input

        while True:  # Infinite loop to gather birth date
            new_bday = input("Enter birth date (MM/DD/YY): ")  # Prompt for birth date
            upper = re.search(r'[A-Z]', new_bday)  # Check for uppercase letters
            lower = re.search(r'[a-z]', new_bday)  # Check for lowercase letters
            if len(new_bday) >= 11:  # If the birth date is too long
                print("Invalid birth date. Please try again.")
            else:
                # Check for invalid characters in birth date
                if upper:  # If it contains uppercase letters
                    print("Please enter only digits. Refer to the required format for the birth date.")
                elif lower:  # If it contains lowercase letters
                    print("Please enter only digits. Refer to the required format for the birth date.")
                else:
                    while True:  # Infinite loop for year level input
                        new_year_lvl = input("Enter Student year level (11 or 12): ")  # Prompt for year level

                        if new_year_lvl == "11":  # If the student is in year 11
                            while True:  # Infinite loop for semester input
                                new_sem = input("Enter semester (1st or 2nd): ").upper()  # Prompt for semester
                                if new_sem == "1ST":  # If the first semester is chosen
                                    num = 0  # Counter for subjects
                                    print("Subjects to take:")  # Title for subject list
                                    print("-------------------------")  # Divider line
                                    # List subjects for the first semester of year 11
                                    for subs in (a, b, c, d, e, f, g, h, i):
                                        num += 1
                                        print(f'{num}. {subs}')  # Print each subject
                                    print("-------------------------")  # Divider line

                                    irregular_student_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                          {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_id,
                                                                           "Subjects": {},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade}})
                                    num = 0
                                    for subject in [a, b, c, d, e, f, g, h, i]:
                                        num += 1
                                        print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                        while True:
                                            choose_sub = input("Yes or No: ").lower()
                                            if choose_sub == "yes":
                                                irregular_student_enrolled.update_one({"ID": find_id},
                                                                                      {"$set": {
                                                                                          f"Subjects.{subject}": 0}})

                                                find_sub_teacher = sub_teacher_in_db.find_one(
                                                    {"Subject To Handle": subject})
                                                if find_sub_teacher:
                                                    student_info = {"ID": find_id, "FirstName": new_fn, "LastName": new_ln}

                                                    # Check if the student is already in the list before adding
                                                    if sub_teacher_in_db.count_documents(
                                                            {"Subject To Handle": subject,
                                                             "Students.ID": find_id}) == 0:
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": subject},
                                                            {"$push": {"Students": student_info}})
                                                else:
                                                    print(f'No teacher has been assigned to {subject} yet')

                                                break  # Exit the inner loop to move to the next subject

                                            elif choose_sub == "no":

                                                if sub_teacher_in_db.count_documents(
                                                        {"Subject To Handle": subject, "Students": find_id}) > 1:
                                                    sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                 {"$pull": {"Students": find_id}})
                                                else:
                                                    print()

                                                break
                                            else:
                                                print("Please refer to the guide for input instructions.")

                                        print("")

                                    break
                                elif new_sem == "2ND":
                                    num = 0  # Counter for subjects
                                    print("Subjects to take:")  # Title for subject list
                                    print("-------------------------")  # Divider line
                                    # List subjects for the first semester of year 11
                                    for subs in (j, k, l, m, n, o, p, q, r):
                                        num += 1
                                        print(f'{num}. {subs}')  # Print each subject
                                    print("-------------------------")  # Divider line

                                    irregular_student_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                          {"$set": {"FirstName": new_fn,
                                                                                    "MiddleName": new_mn,
                                                                                    "LastName": new_ln,
                                                                                    "BirthDate": new_bday,
                                                                                    "ID": find_id,
                                                                                    "Subjects": {},
                                                                                    "Year Level": new_year_lvl,
                                                                                    "Sem": new_sem,
                                                                                    "Final Grade": grade}})
                                    num = 0
                                    for subject in [j, k, l, m, n, o, p, q, r]:
                                        num += 1
                                        print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                        while True:
                                            choose_sub = input("Yes or No: ").lower()
                                            if choose_sub == "yes":
                                                irregular_student_enrolled.update_one({"ID": find_id},
                                                                                      {"$set": {
                                                                                          f"Subjects.{subject}": 0}})

                                                find_sub_teacher = sub_teacher_in_db.find_one(
                                                    {"Subject To Handle": subject})
                                                if find_sub_teacher:
                                                    student_info = {"ID": find_id, "FirstName": new_fn,
                                                                    "LastName": new_ln}

                                                    # Check if the student is already in the list before adding
                                                    if sub_teacher_in_db.count_documents(
                                                            {"Subject To Handle": subject,
                                                             "Students.ID": find_id}) == 0:
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": subject},
                                                            {"$push": {"Students": student_info}})
                                                else:
                                                    print(f'No teacher has been assigned to {subject} yet.')

                                                break  # Exit the inner loop to move to the next subject

                                            elif choose_sub == "no":

                                                if sub_teacher_in_db.count_documents(
                                                        {"Subject To Handle": subject, "Students": find_id}) > 1:
                                                    sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                 {"$pull": {"Students": find_id}})
                                                else:
                                                    print()

                                                break
                                            else:
                                                print("Please refer to the guide for input instructions.")

                                        print("")

                                    break
                                else:
                                    print("Please enter a valid semester: '1st' or '2nd'.")
                            break
                        elif new_year_lvl == "12":  # If the student is in year 11
                            while True:  # Infinite loop for semester input
                                new_sem = input("Enter semester (1st or 2nd): ").upper()  # Prompt for semester
                                if new_sem == "1ST":  # If the first semester is chosen
                                    num = 0  # Counter for subjects
                                    print("Subjects to take:")  # Title for subject list
                                    print("-------------------------")  # Divider line
                                    # List subjects for the first semester of year 11
                                    for subs in (s, t, u, v, w, x, y, z):
                                        num += 1
                                        print(f'{num}. {subs}')  # Print each subject
                                    print("-------------------------")  # Divider line

                                    irregular_student_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                          {"$set": {"FirstName": new_fn,
                                                                           "MiddleName": new_mn,
                                                                           "LastName": new_ln,
                                                                           "BirthDate": new_bday,
                                                                           "ID": find_id,
                                                                           "Subjects": {},
                                                                           "Year Level": new_year_lvl,
                                                                           "Sem": new_sem,
                                                                           "Final Grade": grade}})
                                    num = 0
                                    for subject in [s, t, u, v, w, x, y, z]:
                                        num += 1
                                        print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                        while True:
                                            choose_sub = input("Yes or No: ").lower()
                                            if choose_sub == "yes":
                                                irregular_student_enrolled.update_one({"ID": find_id},
                                                                                      {"$set": {
                                                                                          f"Subjects.{subject}": 0}})

                                                find_sub_teacher = sub_teacher_in_db.find_one(
                                                    {"Subject To Handle": subject})
                                                if find_sub_teacher:
                                                    student_info = {"ID": find_id, "FirstName": new_fn, "LastName": new_ln}

                                                    # Check if the student is already in the list before adding
                                                    if sub_teacher_in_db.count_documents(
                                                            {"Subject To Handle": subject,
                                                             "Students.ID": find_id}) == 0:
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": subject},
                                                            {"$push": {"Students": student_info}})
                                                else:
                                                    print(f'No teacher has been assigned to {subject} yet.')

                                                break  # Exit the inner loop to move to the next subject

                                            elif choose_sub == "no":

                                                if sub_teacher_in_db.count_documents(
                                                        {"Subject To Handle": subject, "Students": find_id}) > 1:
                                                    sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                 {"$pull": {"Students": find_id}})
                                                else:
                                                    print()

                                                break
                                            else:
                                                print("Please refer to the guide for input instructions.")

                                        print("")

                                    break
                                elif new_sem == "2ND":
                                    num = 0  # Counter for subjects
                                    print("Subjects to take:")  # Title for subject list
                                    print("-------------------------")  # Divider line
                                    # List subjects for the first semester of year 11
                                    for subs in (aa, ab, ac, ad, ae, af, ag, ah, ai):
                                        num += 1
                                        print(f'{num}. {subs}')  # Print each subject
                                    print("-------------------------")  # Divider line

                                    irregular_student_enrolled.update_one({"FirstName": find_fn, "ID": find_id},
                                                                          {"$set": {"FirstName": new_fn,
                                                                                    "MiddleName": new_mn,
                                                                                    "LastName": new_ln,
                                                                                    "BirthDate": new_bday,
                                                                                    "ID": find_id,
                                                                                    "Subjects": {},
                                                                                    "Year Level": new_year_lvl,
                                                                                    "Sem": new_sem,
                                                                                    "Final Grade": grade}})
                                    num = 0
                                    for subject in [aa, ab, ac, ad, ae, af, ag, ah, ai]:
                                        num += 1
                                        print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                        while True:
                                            choose_sub = input("Yes or No: ").lower()
                                            if choose_sub == "yes":
                                                irregular_student_enrolled.update_one({"ID": find_id},
                                                                                      {"$set": {
                                                                                          f"Subjects.{subject}": 0}})

                                                find_sub_teacher = sub_teacher_in_db.find_one(
                                                    {"Subject To Handle": subject})
                                                if find_sub_teacher:
                                                    student_info = {"ID": find_id, "FirstName": new_fn,
                                                                    "LastName": new_ln}

                                                    # Check if the student is already in the list before adding
                                                    if sub_teacher_in_db.count_documents(
                                                            {"Subject To Handle": subject,
                                                             "Students.ID": find_id}) == 0:
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": subject},
                                                            {"$push": {"Students": student_info}})
                                                else:
                                                    print(f'No teacher has been assigned to {subject} yet')

                                                break  # Exit the inner loop to move to the next subject

                                            elif choose_sub == "no":

                                                if sub_teacher_in_db.count_documents(
                                                        {"Subject To Handle": subject, "Students": find_id}) > 1:
                                                    sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                 {"$pull": {"Students": find_id}})
                                                else:
                                                    print()

                                                break
                                            else:
                                                print("Please refer to the guide for input instructions.")

                                        print("")

                                    break
                                else:
                                    print("Please enter a valid semester: '1st' or '2nd'.")
                            break
                        else:
                            print("Please enter a valid year level: '11' or '12'.")

                    print("----------------------------")  # Divider line
                    print(" UPDATE ACCOUNT FOR STUDENT ")  # Title for account creation
                    print("----------------------------")  # Divider line

                    find_student_to_upd_account = irregular_student_enrolled.find_one(
                        {"FirstName": new_fn, "LastName": new_ln, "ID": find_id})  # Check if student exists

                    if find_student_to_upd_account:  # If the student exists
                        while True:  # Infinite loop for username input
                            new_username = input(
                                "Please enter a username (must have at least 8 characters): ").upper()  # Prompt for username
                            if len(new_username) <= 7:  # Check username length
                                print("Username must be at least 8 characters long. Please try again.")  # Inform user of error
                            else:
                                while True:  # Infinite loop for password input
                                    new_password = input("Enter a Password (must be at least 6 characters long, include an uppercase letter, a lowercase letter, and a digit): ")  # Prompt for password
                                    # Check if password exists in any collection
                                    find_password = (((students_enrolled.find_one({"Password": new_password}) or
                                                       irregular_student_enrolled.find_one(
                                                           {"Password": new_password})) or
                                                      teacher_in_db.find_one({"Password": new_password})) or
                                                     sub_teacher_in_db.find_one({"Password": new_password}))

                                    if len(new_password) <= 5:  # Check password length
                                        print("Password must be at least 6 characters long. Please try again.")  # Inform user of error
                                    elif find_password:  # If password already exists
                                        print("Password already exists. Please try again.")  # Inform user of error
                                    else:
                                        # Check password criteria
                                        upper = re.search(r'[A-Z]', new_password)  # Check for uppercase letters
                                        lower = re.search(r'[a-z]', new_password)  # Check for lowercase letters
                                        numbers = re.search(r'[0-9]', new_password)  # Check for digits

                                        if not upper:  # If no uppercase letters
                                            print("Password must include an uppercase letter. Please try again.")
                                        elif not lower:  # If no lowercase letters
                                            print("Password must include a lower letter. Please try again.")
                                        else:
                                            if not numbers:
                                                print("Password must include digit. Please try again")
                                            else:
                                                # Update the student's username and password in the database
                                                irregular_student_enrolled.update_one(
                                                    {"FirstName": new_fn, "ID": find_id},
                                                    {"$set": {"Username": new_username, "Password": new_password}})
                                                print(f'Student ID: {find_id}, has been updated')  # Confirmation message
                                                print("")  # Print a blank line for spacing

                                                while True:  # Infinite loop for enrollment option
                                                    opt = input(
                                                        "Do you want to update another student? (yes/no): ").lower()  # Prompt for another enrollment
                                                    if opt == "yes":  # If user wants to enroll another student
                                                        update_student()  # Recursive call to enroll another student
                                                        break  # Exit loop
                                                    elif opt == "no":  # If user does not want to enroll another student
                                                        admin_dashboard()  # Redirect to admin dashboard
                                                        break  # Exit loop
                                                    else:
                                                        print(
                                                            "Invalid input. Please enter 'yes' or 'no'.")  # Inform user of incorrect input
                                            break  # Exit password input loop
                                break  # Exit username input loop
                    else:
                        print("Student record not found.")

def enroll_student():
    # Function to enroll a student in the system
    global advisory, section_in, i, subs  # Global variables for use within the function
    global subject  # Global variable for subject handling
    print("***ENROLLMENT SECTION***")  # Title of the enrollment section
    print("")  # Print a blank line for spacing
    print("Please follow the steps to enroll!!")  # Instructions for the enrollment process
    print("")  # Print a blank line for spacing

    while True:  # Infinite loop to handle the enrollment process
        print("")  # Print a blank line for spacing
        print("STUDENT INFORMATION")  # Title for student information input
        while True:  # Infinite loop to gather student ID
            id = input("Enter student ID (6-digit ID): ").strip()  # Prompt for student ID

            # Check for invalid characters in the ID
            letter1 = re.search(r'[a-z]', id)  # Check for lowercase letters
            letter2 = re.search(r'[A-Z]', id)  # Check for uppercase letters

            # Check if the ID already exists in the enrolled or irregular students or teacher collections
            if students_enrolled.find_one({"ID": id}):
                print("Student ID already exists.")
            elif irregular_student_enrolled.find_one({"ID": id}):
                print("Student ID already exists.")
            elif teacher_in_db.find_one({"ID": id}):
                print("ID already exists.")
            elif sub_teacher_in_db.find_one({"ID": id}):
                print("ID already exists.")
            elif letter1:  # If the ID contains lowercase letters
                print("Only accepts digits. Please try again.")
            elif letter2:  # If the ID contains uppercase letters
                print("Only accepts digits. Please try again.")
            else:
                # Check the length of the ID
                if len(id) <= 5 or len(id) > 6:
                    print("ID must be complete. Please try again.")
                else:
                    # Prompt for student names
                    fn = input("Enter student's first name: ").upper().strip()  # First name input
                    mn = input("Enter student's middle name: ").upper().strip() # Middle name input
                    ln = input("Enter student's last name: ").upper().strip()  # Last name input

                    while True:  # Infinite loop to gather birth date
                        bday = input("Enter birth date (MM/DD/YY): ").strip()  # Prompt for birth date
                        upper = re.search(r'[A-Z]', bday)  # Check for uppercase letters
                        lower = re.search(r'[a-z]', bday)  # Check for lowercase letters
                        if len(bday) >= 11:  # If the birth date is too long
                            print("Invalid birth date. Please try again.")
                        else:
                            # Check for invalid characters in birth date
                            if upper:  # If it contains uppercase letters
                                print("Only digits will be accepted. Please try again.")
                            elif lower:  # If it contains lowercase letters
                                print("Only digits will be accepted. Please try again.")
                            else:
                                while True:  # Infinite loop for year level input
                                    year_lvl = input("Enter Student year level (11 or 12): ").strip()  # Prompt for year level

                                    if year_lvl == "11":  # If the student is in year 11
                                        while True:  # Infinite loop for semester input
                                            sem = input("Enter semester (1st or 2nd): ").upper().strip()  # Prompt for semester
                                            if sem == "1ST":  # If the first semester is chosen
                                                num = 0  # Counter for subjects
                                                print("Subjects to take:")  # Title for subject list
                                                print("-------------------------")  # Divider line
                                                # List subjects for the first semester of year 11
                                                for subs in (a, b, c, d, e, f, g, h, i):
                                                    num += 1
                                                    print(f'{num}. {subs}')  # Print each subject
                                                print("-------------------------")  # Divider line

                                                # Insert the student data into the database
                                                students_enrolled.insert_one({
                                                    "FirstName": fn,
                                                    "MiddleName": mn,
                                                    "LastName": ln,
                                                    "BirthDate": bday,
                                                    "ID": id,
                                                    "Subjects": {a: 0, b: 0, c: 0, d: 0, e: 0, f: 0, g: 0, h: 0, i: 0},
                                                    "Year Level": year_lvl,
                                                    "Sem": sem,
                                                    "Final Grade": grade,
                                                    "StudentStatus": "Regular Student"
                                                })

                                                # Update each subject teacher with the new student info
                                                for sub_teacher in [a, b, c, d, e, f, g, h, i]:
                                                    find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                                    if find_sub_teacher > 0:
                                                        student_info = {"ID": id, "FirstName": fn, "LastName": ln}
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": sub_teacher},
                                                            {"$push": {"Students": student_info}})  # Add student to teacher's list
                                                    else:
                                                        print(f'No teacher has been assigned to {sub_teacher} yet.')
                                                break  # Exit semester input loop

                                            elif sem == "2ND":  # If the second semester is chosen
                                                num = 0  # Counter for subjects
                                                print("Subjects to take:")  # Title for subject list
                                                print("-------------------------")  # Divider line
                                                # List subjects for the second semester of year 11
                                                for subs in (j, k, l, m, n, o, p, q, r):
                                                    num += 1
                                                    print(f'{num}. {subs}')  # Print each subject
                                                print("-------------------------")  # Divider line

                                                # Insert the student data into the database
                                                students_enrolled.insert_one({
                                                    "FirstName": fn,
                                                    "MiddleName": mn,
                                                    "LastName": ln,
                                                    "BirthDate": bday,
                                                    "ID": id,
                                                    "Subjects": {j: 0, k: 0, l: 0, m: 0, n: 0, o: 0, p: 0, q: 0, r: 0},
                                                    "Year Level": year_lvl,
                                                    "Sem": sem,
                                                    "Final Grade": grade,
                                                    "StudentStatus": "Regular Student"
                                                })

                                                # Update each subject teacher with the new student info
                                                for sub_teacher in [j, k, l, m, n, o, p, q, r]:
                                                    find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                                    if find_sub_teacher > 0:
                                                        student_info = {"ID": id, "FirstName": fn, "LastName": ln}
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": sub_teacher},
                                                            {"$push": {"Students": student_info}})  # Add student to teacher's list
                                                    else:
                                                        print(f'No teacher has been assigned to {sub_teacher} yet. ')
                                                break  # Exit semester input loop
                                            else:
                                                print("Please refer to the provided sample. Try again.")  # Inform user of incorrect input
                                        break  # Exit year level input loop

                                    elif year_lvl == "12":  # If the student is in year 12
                                        while True:  # Infinite loop for semester input
                                            sem = input("Enter semester (1st or 2nd): ").upper().strip()  # Prompt for semester
                                            if sem == "1ST":  # If the first semester is chosen
                                                num = 0  # Counter for subjects
                                                print("Subjects to take:")  # Title for subject list
                                                # List subjects for the first semester of year 12
                                                print("-------------------------")
                                                for subs in (s, t, u, v, w, x, y, z):
                                                    num += 1
                                                    print(f'{num}. {subs}')  # Print each subject
                                                print("-------------------------")  # Divider line

                                                # Insert the student data into the database
                                                students_enrolled.insert_one({
                                                    "FirstName": fn,
                                                    "MiddleName": mn,
                                                    "LastName": ln,
                                                    "BirthDate": bday,
                                                    "ID": id,
                                                    "Subjects": {s: 0, t: 0, u: 0, v: 0, w: 0, x: 0, y: 0, z: 0},
                                                    "Year Level": year_lvl,
                                                    "Sem": sem,
                                                    "Final Grade": grade,
                                                    "StudentStatus": "Regular Student"
                                                })

                                                # Update each subject teacher with the new student info
                                                for sub_teacher in [s, t, u, v, w, x, y, z]:
                                                    find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                                    if find_sub_teacher > 0:
                                                        student_info = {"ID": id, "FirstName": fn, "LastName": ln}
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": sub_teacher},
                                                            {"$push": {"Students": student_info}})  # Add student to teacher's list
                                                    else:
                                                        print(f'No teacher has been assigned to {sub_teacher} yet')
                                                break  # Exit semester input loop

                                            elif sem == "2ND":  # If the second semester is chosen
                                                num = 0  # Counter for subjects
                                                print("Subjects to take:")  # Title for subject list
                                                # List subjects for the second semester of year 12
                                                print("-------------------------")
                                                for subs in (aa, ab, ac, ad, ae, af, ag, ah, ai):
                                                    num += 1
                                                    print(f'{num}. {subs}')  # Print each subject
                                                print("-------------------------")  # Divider line

                                                # Insert the student data into the database
                                                students_enrolled.insert_one({
                                                    "FirstName": fn,
                                                    "MiddleName": mn,
                                                    "LastName": ln,
                                                    "BirthDate": bday,
                                                    "ID": id,
                                                    "Subjects": {aa: 0, ab: 0, ac: 0, ad: 0, ae: 0, af: 0, ag: 0, ah: 0, ai: 0},
                                                    "Year Level": year_lvl,
                                                    "Sem": sem,
                                                    "Final Grade": grade,
                                                    "StudentStatus": "Regular Student"
                                                })

                                                # Update each subject teacher with the new student info
                                                for sub_teacher in [aa, ab, ac, ad, ae, af, ag, ah, ai]:
                                                    find_sub_teacher = sub_teacher_in_db.count_documents({"Subject To Handle": sub_teacher})
                                                    if find_sub_teacher > 0:
                                                        student_info = {"ID": id, "FirstName": fn, "LastName": ln}
                                                        sub_teacher_in_db.update_one(
                                                            {"Subject To Handle": sub_teacher},
                                                            {"$push": {"Students": student_info}})  # Add student to teacher's list
                                                    else:
                                                        print(f'No teacher has been assigned to {sub_teacher} yet.')
                                                break  # Exit semester input loop
                                            else:
                                                print("Please refer to the provided sample. Try again.")  # Inform user of incorrect input
                                        break  # Exit year level input loop
                                    else:
                                        print("Please enter a valid year level: '11' or '12'.")  # Inform user of incorrect input

                                print("-------------------------")  # Divider line
                                print(" ADD ACCOUNT FOR STUDENT ")  # Title for account creation
                                print("-------------------------")  # Divider line

                                find_student_to_make_account = students_enrolled.find({"FirstName": fn, "ID": id})  # Check if student exists

                                if find_student_to_make_account:  # If the student exists
                                    while True:  # Infinite loop for username input
                                        username = input("Enter a username (must be at least 8 characters): ").upper().strip()  # Prompt for username
                                        if len(username) <= 7:  # Check username length
                                            print("Username must be at least 8 characters long. Please try again.")  # Inform user of error
                                        else:
                                            while True:  # Infinite loop for password input
                                                password = input("Enter a Password (must be at least 6 characters long, include an uppercase letter, a lowercase letter, and a digit): ").strip()  # Prompt for password
                                                # Check if password exists in any collection
                                                find_password = (((students_enrolled.find_one({"Password": password}) or
                                                                 irregular_student_enrolled.find_one({"Password": password})) or
                                                                 teacher_in_db.find_one({"Password": password})) or
                                                                 sub_teacher_in_db.find_one({"Password": password}))

                                                if len(password) <= 5:  # Check password length
                                                    print("Password must be at least 6 characters long. Please try again.")  # Inform user of error
                                                elif find_password:  # If password already exists
                                                    print("Password already exists. Please try again.")  # Inform user of error
                                                else:
                                                    # Check password criteria
                                                    upper = re.search(r'[A-Z]', password)  # Check for uppercase letters
                                                    lower = re.search(r'[a-z]', password)  # Check for lowercase letters
                                                    numbers = re.search(r'[0-9]', password)  # Check for digits

                                                    if not upper:  # If no uppercase letters
                                                        print("Password must include an uppercase letter. Please try again.")
                                                    elif not lower:  # If no lowercase letters
                                                        print("Password must include a lower letter. Please try again.")
                                                    else:
                                                        if not numbers:
                                                            print("Password must include a lower letter. Please try again")
                                                        else:
                                                            # Update the student's username and password in the database
                                                            students_enrolled.update_one(
                                                                {"FirstName": fn, "ID": id},
                                                                {"$set": {"Username": username, "Password": password}})
                                                            print("Student has been enrolled")  # Confirmation message
                                                            print("")  # Print a blank line for spacing

                                                            get_list_of_students = students_enrolled.find()
                                                            nums = 0
                                                            print("Enrolled Students:")
                                                            print("--------------------------")
                                                            for students in get_list_of_students:
                                                                nums += 1
                                                                print(f'{nums}. First Name: {students.get("FirstName")} | Last Name: {students.get("LastName")} | ID: {students.get("ID")}')
                                                            print("---------------------------")

                                                            print(f'{id}, has been enrolled.')


                                                            while True:  # Infinite loop for enrollment option
                                                                opt = input("Do you want to enroll another student? (yes or no): ").lower().strip()  # Prompt for another enrollment
                                                                if opt == "yes":  # If user wants to enroll another student
                                                                    enroll_student()  # Recursive call to enroll another student
                                                                    break  # Exit loop
                                                                elif opt == "no":  # If user does not want to enroll another student
                                                                    admin_dashboard()  # Redirect to admin dashboard
                                                                    break  # Exit loop
                                                                else:
                                                                    print("Please refer to the provided sample. Try again.")  # Inform user of incorrect input
                                                        break  # Exit password input loop
                                            break  # Exit username input loop

def enroll_irregular_student():
    global advisory, section_in, i, subs
    global subject

    print("STUDENT INFORMATION")

    while True:
        id = input("Enter student ID (6-digit ID): ")

        letter1 = re.search(r'[a-z]', id)
        letter2 = re.search(r'[A-Z]', id)

        if irregular_student_enrolled.find_one({"ID": id}):
            print("Student ID already exist.")
        elif students_enrolled.find_one({"ID": id}):
            print("Student ID already exist.")
        elif teacher_in_db.find_one({"ID": id}):
            print("ID already exist.")
        elif sub_teacher_in_db.find_one({"ID": id}):
            print("ID already exist.")
        elif letter1:
            print("Only accepts digits. Please try again.")
        elif letter2:
            print("Only accepts digits. Please try again.")

        else:
            if len(id) <= 5 or len(id) > 6:
                print("Id must be complete. Please try again.")
            else:
                fn = input("Enter students first name: ").upper().strip()
                mn = input("Enter students middle name: ").upper().strip()
                ln = input("Enter students last name: ").upper().strip()
                while True:
                    bday = input("Enter birth date (MM/DD/YY): ").strip()
                    upper = re.search(r'[A-Z]', bday)
                    lower = re.search(r'[a-z]', bday)
                    if len(bday) >= 11:
                        print("Invalid birth date. Please try again.")
                    else:
                        if upper:
                            print("Only digits will be accepted. Please try again.")
                        elif lower:
                            print("Only digits will be accepted. Please try again.")
                        else:
                            while True:
                                year_lvl = input("Enter Student year level (11 or 12): ").strip()

                                if year_lvl == "11":
                                    while True:
                                        sem = input("Enter semester (1st or 2nd): ").upper().strip()
                                        if sem == "1ST":
                                            num = 0
                                            print("Available Subjects for Enrollment:")
                                            print("-------------------------")
                                            for subs in (a, b, c, d, e, f, g, h, i):
                                                num += 1
                                                print(f'{num}. {subs}')
                                            print("-------------------------")

                                            irregular_student_enrolled.insert_one({"FirstName": fn,
                                                                                   "MiddleName": mn,
                                                                                   "LastName": ln,
                                                                                   "BirthDate": bday,
                                                                                   "ID": id,
                                                                                   "Subjects": {},
                                                                                   "Year Level": year_lvl,
                                                                                   "Sem": sem,
                                                                                   "Final Grade": grade})
                                            num = 0
                                            for subject in [a, b, c, d, e, f, g, h, i]:
                                                num += 1
                                                print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                                while True:
                                                    choose_sub = input("Yes or No: ").lower().strip()
                                                    if choose_sub == "yes":
                                                        irregular_student_enrolled.update_one({"ID": id},
                                                                                              {"$set": {f"Subjects.{subject}": 0}})

                                                        find_sub_teacher = sub_teacher_in_db.find_one(
                                                            {"Subject To Handle": subject})
                                                        if find_sub_teacher:
                                                            student_info = {"ID": id, "FirstName": fn, "LastName": ln}

                                                            # Check if the student is already in the list before adding
                                                            if sub_teacher_in_db.count_documents(
                                                                    {"Subject To Handle": subject,
                                                                     "Students.ID": id}) == 0:
                                                                sub_teacher_in_db.update_one(
                                                                    {"Subject To Handle": subject},
                                                                    {"$push": {"Students": student_info}})
                                                        else:
                                                            print(f'No teacher has been assigned to {subject} yet.')

                                                        break  # Exit the inner loop to move to the next subject

                                                    elif choose_sub == "no":

                                                        if sub_teacher_in_db.count_documents(
                                                                {"Subject To Handle": subject, "Students": id}) > 1:
                                                            sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                         {"$pull": {"Students": id}})
                                                        else:
                                                            print()

                                                        break
                                                    else:
                                                        print("Please refer to the guide for input instructions.")

                                                print("")

                                            break


                                        elif sem == "2ND":
                                            num = 0
                                            print("Available Subjects for Enrollment:")
                                            print("-------------------------")
                                            for subs in (j, k, l, m, n, o, p, q, r):
                                                num += 1
                                                print(f'{num}. {subs}')
                                            print("-------------------------")

                                            irregular_student_enrolled.insert_one({"FirstName": fn,
                                                                                   "MiddleName": mn,
                                                                                   "LastName": ln,
                                                                                   "BirthDate": bday,
                                                                                   "ID": id,
                                                                                   "Subjects": {},
                                                                                   "Year Level": year_lvl,
                                                                                   "Sem": sem,
                                                                                   "Final Grade": grade})

                                            num = 0
                                            for subject in [j, k, l, m, n, o, p, q, r]:
                                                num += 1
                                                print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                                while True:
                                                    choose_sub = input("Yes or no (yes/no): ").lower().strip()
                                                    if choose_sub == "yes":
                                                        irregular_student_enrolled.update_one({"ID": id},
                                                                                              {"$set": {
                                                                                                  f"Subjects.{subject}": 0}})
                                                        find_sub_teacher = sub_teacher_in_db.find_one(
                                                            {"Subject To Handle": subject})
                                                        if find_sub_teacher:
                                                            student_info = {"ID": id, "FirstName": fn, "LastName": ln}

                                                            # Check if the student is already in the list before adding
                                                            if sub_teacher_in_db.count_documents(
                                                                    {"Subject To Handle": subject,
                                                                     "Students.ID": id}) == 0:
                                                                sub_teacher_in_db.update_one(
                                                                    {"Subject To Handle": subject},
                                                                    {"$push": {"Students": student_info}})
                                                        else:
                                                            print(f'No teacher has been assigned to {subject} yet')

                                                        break  # Exit the inner loop to move to the next subject

                                                    elif choose_sub == "no":

                                                        if sub_teacher_in_db.count_documents(
                                                                {"Subject To Handle": subject, "Students": id}) > 1:
                                                            sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                         {"$pull": {"Students": id}})
                                                        else:
                                                            print()

                                                        break
                                                    else:
                                                        print("Please refer to the guide for input instructions.")

                                                    print("")

                                            break
                                        else:
                                            print("Please refer to the provided sample.")
                                    break

                                elif year_lvl == "12":
                                    while True:
                                        sem = input("Enter semester (1st or 2nd): ").upper().strip()
                                        if sem == "1ST":
                                            num = 0
                                            print("Available Subjects for Enrollment:")
                                            print("-------------------------")
                                            for subs in (s,t,u,v,w,x,y,z):
                                                num += 1
                                                print(f'{num}. {subs}')
                                            print("-------------------------")

                                            irregular_student_enrolled.insert_one({"FirstName": fn,
                                                                                   "MiddleName": mn,
                                                                                   "LastName": ln,
                                                                                   "BirthDate": bday,
                                                                                   "ID": id,
                                                                                   "Subjects": {},
                                                                                   "Year Level": year_lvl,
                                                                                   "Sem": sem,
                                                                                   "Final Grade": grade})
                                            num = 0
                                            for subject in [s,t,u,v,w,x,y,z]:
                                                num += 1
                                                print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                                while True:
                                                    choose_sub = input("Yes or no (yes/no): ").lower().strip()
                                                    if choose_sub == "yes":
                                                        irregular_student_enrolled.update_one({"ID": id},
                                                                                              {"$set": {
                                                                                                  f"Subjects.{subject}": 0}})
                                                        find_sub_teacher = sub_teacher_in_db.find_one(
                                                            {"Subject To Handle": subject})
                                                        if find_sub_teacher:
                                                            student_info = {"ID": id, "FirstName": fn, "LastName": ln}

                                                            # Check if the student is already in the list before adding
                                                            if sub_teacher_in_db.count_documents(
                                                                    {"Subject To Handle": subject,
                                                                     "Students.ID": id}) == 0:
                                                                sub_teacher_in_db.update_one(
                                                                    {"Subject To Handle": subject},
                                                                    {"$push": {"Students": student_info}})
                                                        else:
                                                            print(f'No teacher has been assigned to {subject} yet.')

                                                        break  # Exit the inner loop to move to the next subject

                                                    elif choose_sub == "no":

                                                        if sub_teacher_in_db.count_documents(
                                                                {"Subject To Handle": subject, "Students": id}) > 1:
                                                            sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                         {"$pull": {"Students": id}})
                                                        else:
                                                            print()

                                                        break
                                                    else:
                                                        print("Please refer to the guide for input instructions.")

                                                    print("")

                                            break


                                        elif sem == "2ND":
                                            num = 0
                                            print("Available Subjects for Enrollment:")
                                            print("-------------------------")
                                            for subs in (aa,ab,ac,ad,ae,af,ag,ah,ai):
                                                num += 1
                                                print(f'{num}. {subs}')
                                            print("-------------------------")

                                            irregular_student_enrolled.insert_one({"FirstName": fn,
                                                                                   "MiddleName": mn,
                                                                                   "LastName": ln,
                                                                                   "BirthDate": bday,
                                                                                   "ID": id,
                                                                                   "Subjects": {},
                                                                                   "Year Level": year_lvl,
                                                                                   "Sem": sem,
                                                                                   "Final Grade": grade})

                                            num = 0
                                            for subject in [aa,ab,ac,ad,ae,af,ag,ah,ai]:
                                                num += 1
                                                print(f"{num}. Do you want to enroll to this subject? ({subject})")
                                                while True:
                                                    choose_sub = input("Yes or no (yes/no): ").lower().strip()
                                                    if choose_sub == "yes":
                                                        irregular_student_enrolled.update_one({"ID": id},
                                                                                              {"$set": {
                                                                                                  f"Subjects.{subject}": 0}})
                                                        find_sub_teacher = sub_teacher_in_db.find_one(
                                                            {"Subject To Handle": subject})
                                                        if find_sub_teacher:
                                                            student_info = {"ID": id, "FirstName": fn, "LastName": ln}

                                                            # Check if the student is already in the list before adding
                                                            if sub_teacher_in_db.count_documents(
                                                                    {"Subject To Handle": subject,
                                                                     "Students.ID": id}) == 0:
                                                                sub_teacher_in_db.update_one(
                                                                    {"Subject To Handle": subject},
                                                                    {"$push": {"Students": student_info}})
                                                        else:
                                                            print(f'No teacher has been assigned to {subject} yet.')

                                                        break  # Exit the inner loop to move to the next subject

                                                    elif choose_sub == "no":

                                                        if sub_teacher_in_db.count_documents(
                                                                {"Subject To Handle": subject, "Students": id}) > 1:
                                                            sub_teacher_in_db.update_one({"Subject To Handle": subject},
                                                                                         {"$pull": {"Students": id}})
                                                        else:
                                                            print()

                                                        break
                                                    else:
                                                        print("Please refer to the guide for input instructions.")

                                                    print("")

                                            break
                                        else:
                                            print("Please refer to the provided sample.")
                                    break
                                else:
                                    print("Please refer to the provided sample.")

                            print("-------------------------")
                            print(" ADD ACCOUNT FOR STUDENT ")
                            print("-------------------------")

                            find_student_to_make_account = irregular_student_enrolled.find_one({"FirstName": fn, "ID": id})

                            if find_student_to_make_account:
                                while True:
                                    username = input("Please enter a username (must be at least 8 characters): ").upper().strip()
                                    if len(username) <= 7:
                                        print("Username must be at least 8 characters long.")
                                    else:
                                        while True:
                                            password = input("Please enter a password (must be at least 6 characters long, include an uppercase letter, a lowercase letter, and a digit): ").strip()
                                            find_password = (((students_enrolled.find_one({"Password": password}) or
                                                               irregular_student_enrolled.find_one({"Password": password})) or
                                                              teacher_in_db.find_one({"Password": password})) or
                                                             sub_teacher_in_db.find_one({"Password": password}))
                                            if len(password) <= 5:
                                                print("Password must be at least 6 characters long.")
                                            elif find_password:
                                                print("Password already exists. Please try again.")
                                            else:

                                                upper = re.search(r'[A-Z]', password)
                                                lower = re.search(r'[a-z]', password)
                                                numbers = re.search(r'[0-10]', password)

                                                if not upper:
                                                    print("Password must include an uppercase letter. Please try again.")
                                                elif not lower:
                                                    print("Password must include a lower letter. Please try again.")
                                                else:
                                                    if not numbers:
                                                        print("Password must include digits. Please try again")
                                                    else:
                                                        irregular_student_enrolled.update_one({"FirstName": fn, "ID": id},
                                                                                     {"$set": {"Username": username,
                                                                                               "Password": password}})

                                                        get_list_of_students = irregular_student_enrolled.find()
                                                        nums = 0
                                                        print("Enrolled Students:")
                                                        print("--------------------------")
                                                        for students in get_list_of_students:
                                                            nums += 1
                                                            print(
                                                                f'{nums}. First Name: {students.get("FirstName")} | Last Name: {students.get("LastName")} | ID: {students.get("ID")}')
                                                        print("---------------------------")


                                                        print("Student has been enrolled.")
                                                        print("")
                                                        while True:
                                                            opt = input("Do you want to enroll another student? (yes or no): ").lower().strip()
                                                            if opt == "yes":
                                                                enroll_irregular_student()
                                                                break
                                                            elif opt == "no":
                                                                admin_dashboard()
                                                                break
                                                            else:
                                                                print("Please refer to the sample provided.")
                                        break



def add_sub_teacher():
    global teacher_official_section, sem
    print("***REGISTER TEACHER***")
    print("")

    while True:
        teacher_id = input("Enter teacher's ID (6-digit ID): ")

        letter1 = re.search(r'[a-z]', teacher_id)
        letter2 = re.search(r'[A-Z]', teacher_id)

        if teacher_in_db.find_one({"ID": teacher_id}):
            print("Teacher ID already exist.")
        elif sub_teacher_in_db.find_one({"ID": teacher_id}):
            print("Teacher ID already exist.")
        elif students_enrolled.find_one({"ID": teacher_id}):
            print("ID already exist.")
        elif irregular_student_enrolled.find_one({"ID": teacher_id}):
            print("ID already exist.")
        elif letter1:
            print("Only accepts digits. Please try again.")
        elif letter2:
            print("Only accepts digits. Please try again.")

        else:
            if len(teacher_id) <= 5 or len(teacher_id) > 6:
                print("Id must be complete. Please try again.")
            else:

                fn = input("Enter teacher's first name: ").upper().strip()
                mn = input("Enter teacher's middle name: ").upper().strip()
                ln = input("Enter teacher's last name: ").upper().strip()

                while True:
                    BirthDate = input("Enter birth date (MM/DD/YY): ").strip()
                    upper = re.search(r'[A-Z]', BirthDate)
                    lower = re.search(r'[a-z]', BirthDate)
                    if len(BirthDate) >= 11:
                        print("Invalid birth date. Please try again.")
                    else:
                        if upper:
                            print("Only digits will be accepted. Please try again.")
                        elif lower:
                            print("Only digits will be accepted. Please try again.")
                        else:
                            while True:

                                year_to_handle = input("Enter Year level to handle (11 or 12): ").strip()

                                if year_to_handle == "11":
                                    while True:
                                        semester = input("Enter semester to handle (1st or 2nd): ").lower().strip()
                                        if semester == "1st":
                                            print("")
                                            print("Subjects you are authorized to manage:")
                                            print("---------------------------------------")
                                            num = 0
                                            for sub_to_handle in [a,b,c,d,e,f,g,h,i]:
                                                num += 1
                                                print(f'{num}. {sub_to_handle}')
                                            print("---------------------------------------")

                                            sub_teacher_in_db.insert_one({"FirstName": fn,
                                                                           "MiddleName": mn,
                                                                           "LastName": ln,
                                                                           "BirthDate": BirthDate,
                                                                           "ID": teacher_id,
                                                                           "Subject To Handle": None,
                                                                           "Year Level To Handle": year_to_handle,
                                                                           "Semester In": semester,
                                                                           "Students": [] })



                                            num = 0
                                            for subject in [a, b, c, d, e, f, g, h, i]:
                                                num += 1
                                                if sub_teacher_in_db.count_documents({"Subject To Handle": subject}) == 1:
                                                    print()
                                                else:
                                                    print(f"{num}. Do you want to handle this subject? ({subject})")
                                                    while True:
                                                        choose_sub_to_handle = input("Yes or No: ").lower().strip()
                                                        if choose_sub_to_handle == "yes":

                                                            sub_teacher_in_db.update_one({"ID": teacher_id},
                                                                                                  {"$set": {"Subject To Handle": subject}})

                                                            # for future reference

                                                            find_regular_students = students_enrolled.find({"Subjects." + subject: {"$exists": True}})
                                                            find_irregular_students = irregular_student_enrolled.find({"Subjects." + subject: {"$exists": True}})
                                                            all_students = list(find_irregular_students) + list(find_regular_students)

                                                            if find_regular_students and find_irregular_students:
                                                                for students in all_students:
                                                                    student_info = {"ID": students.get("ID"),
                                                                                    "FirstName": students.get("FirstName"),
                                                                                    "LastName": students.get("LastName")}
                                                                    sub_teacher_in_db.update_one({"ID": teacher_id}, {"$push": {"Students": student_info}})
                                                            else:
                                                                print("No student exists. Please ensure the identification details are correct.")


                                                            add_account_for_subject_teacher(fn, teacher_id)
                                                            return fn, teacher_id,
                                                        elif choose_sub_to_handle == "no":
                                                            break
                                                        else:
                                                            print("Invalid input. Please enter 'yes' or 'no'.")

                                        elif semester == "2nd":
                                            print("")
                                            print("Subjects you are authorized to manage:")
                                            print("---------------------------------------")
                                            num = 0
                                            for sub_to_handle in [j,k,l,m,n,o,p,q,r]:
                                                num += 1
                                                print(f'{num}. {sub_to_handle}')
                                            print("---------------------------------------")

                                            sub_teacher_in_db.insert_one({"FirstName": fn,
                                                                          "MiddleName": mn,
                                                                          "LastName": ln,
                                                                          "BirthDate": BirthDate,
                                                                          "ID": teacher_id,
                                                                          "Subject To Handle": None,
                                                                          "Year Level To Handle": year_to_handle,
                                                                          "Semester In": semester,
                                                                          "Students": []})


                                            num = 0
                                            for subject in [j,k,l,m,n,o,p,q,r]:
                                                num += 1
                                                if sub_teacher_in_db.count_documents({"Subject To Handle": subject}) == 1:
                                                    print()
                                                else:
                                                    print(f"{num}. Do you want to handle this subject? ({subject})")
                                                    while True:
                                                        choose_sub_to_handle = input("Yes or No): ").lower().strip()
                                                        if choose_sub_to_handle == "yes":
                                                            sub_teacher_in_db.update_one({"ID": teacher_id},
                                                                                         {"$set": {
                                                                                             "Subject To Handle": subject}})

                                                            find_regular_students = students_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            find_irregular_students = irregular_student_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            all_students = list(find_irregular_students) + list(
                                                                find_regular_students)

                                                            if find_regular_students and find_irregular_students:
                                                                for students in all_students:
                                                                    student_info = {"ID": students.get("ID"),
                                                                                    "FirstName": students.get("FirstName"),
                                                                                    "LastName": students.get("LastName")}
                                                                    sub_teacher_in_db.update_one({"ID": teacher_id}, {
                                                                        "$push": {"Students": student_info}})
                                                            else:
                                                                print("No student exists. Please ensure the identification details are correct.")

                                                            add_account_for_subject_teacher(fn, teacher_id, )
                                                            return fn, teacher_id
                                                        elif choose_sub_to_handle == "no":
                                                            break
                                                        else:
                                                            print("Invalid input. Please enter 'yes' or 'no'.")

                                        else:
                                            print("Please enter a valid semester: '1st' or '2nd'.")

                                elif year_to_handle == "12":
                                    while True:
                                        semester = input("Enter semester to handle (1st or 2nd): ").lower().strip()
                                        if semester == "1st":
                                            print("")
                                            print("Subjects you are authorized to manage:")
                                            print("---------------------------------------")
                                            num = 0
                                            for sub_to_handle in [s,t,u,v,w,x,y,z]:
                                                num += 1
                                                print(f'{num}. {sub_to_handle}')
                                            print("---------------------------------------")

                                            sub_teacher_in_db.insert_one({"FirstName": fn,
                                                                          "MiddleName": mn,
                                                                          "LastName": ln,
                                                                          "BirthDate": BirthDate,
                                                                          "ID": teacher_id,
                                                                          "Subject To Handle": None,
                                                                          "Year Level To Handle": year_to_handle,
                                                                          "Semester In": semester,
                                                                          "Students": []})

                                            num = 0
                                            for subject in [s, t, u, v, w, x, y, z]:
                                                num += 1
                                                if sub_teacher_in_db.count_documents({"Subject To Handle": subject}) == 1:
                                                    print()
                                                else:
                                                    print(f"{num}. Do you want to handle this subject? ({subject})")
                                                    while True:
                                                        choose_sub_to_handle = input("Yes or No: ").lower().strip()
                                                        if choose_sub_to_handle == "yes":
                                                            sub_teacher_in_db.update_one({"ID": teacher_id},
                                                                                                  {"$set": {"Subject To Handle": subject}})

                                                            find_regular_students = students_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            find_irregular_students = irregular_student_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            all_students = list(find_irregular_students) + list(
                                                                find_regular_students)

                                                            if find_regular_students and find_irregular_students:
                                                                for students in all_students:
                                                                    student_info = {"ID": students.get("ID"),
                                                                                    "FirstName": students.get("FirstName"),
                                                                                    "LastName": students.get("LastName")}
                                                                    sub_teacher_in_db.update_one({"ID": teacher_id}, {
                                                                        "$push": {"Students": student_info}})
                                                            else:
                                                                print("No student exists. Please ensure the identification details are correct.")

                                                            add_account_for_subject_teacher(fn, teacher_id, )
                                                            return fn, teacher_id
                                                        elif choose_sub_to_handle == "no":
                                                            break
                                                        else:
                                                            print("Invalid input. Please enter 'yes' or 'no'.")

                                        elif semester == "2nd":
                                            print("")
                                            print("Subjects you are authorized to manage:")
                                            print("---------------------------------------")
                                            num = 0
                                            for sub_to_handle in [aa,ab,ac,ad,ae,af,ag,ah,ai]:
                                                num += 1
                                                print(f'{num}. {sub_to_handle}')
                                            print("---------------------------------------")

                                            sub_teacher_in_db.insert_one({"FirstName": fn,
                                                                          "MiddleName": mn,
                                                                          "LastName": ln,
                                                                          "BirthDate": BirthDate,
                                                                          "ID": teacher_id,
                                                                          "Subject To Handle": None,
                                                                          "Year Level To Handle": year_to_handle,
                                                                          "Semester In": semester,
                                                                          "Students": []})

                                            num = 0
                                            for subject in [aa,ab,ac,ad,ae,af,ag,ah,ai]:
                                                num += 1
                                                if sub_teacher_in_db.count_documents({"Subject To Handle": subject}) == 1:
                                                    print()
                                                else:
                                                    print(f"{num}. Do you want to handle this subject? ({subject})")
                                                    while True:
                                                        choose_sub_to_handle = input("Yes or No: ").lower().strip()
                                                        if choose_sub_to_handle == "yes":
                                                            sub_teacher_in_db.update_one({"ID": teacher_id},
                                                                                         {"$set": {
                                                                                             "Subject To Handle": subject}})

                                                            find_regular_students = students_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            find_irregular_students = irregular_student_enrolled.find(
                                                                {"Subjects." + subject: {"$exists": True}})
                                                            all_students = list(find_irregular_students) + list(
                                                                find_regular_students)

                                                            if find_regular_students and find_irregular_students:
                                                                for students in all_students:
                                                                    student_info = {"ID": students.get("ID"),
                                                                                    "FirstName": students.get("FirstName"),
                                                                                    "LastName": students.get("LastName")}
                                                                    sub_teacher_in_db.update_one({"ID": teacher_id}, {
                                                                        "$push": {"Students": student_info}})
                                                            else:
                                                                print("No student exists. Please ensure the identification details are correct.")


                                                            add_account_for_subject_teacher(fn, teacher_id)
                                                            return fn, teacher_id

                                                        elif choose_sub_to_handle == "no":
                                                            break
                                                        else:
                                                            print("Invalid input. Please enter 'yes' or 'no'.")
                                        else:
                                            print("Please enter a valid semester: '1st' or '2nd'.")
                                else:
                                    print("Please enter a valid year level: '11' or '12'.")

def add_account_for_subject_teacher(fn, teacher_id):

    print("---------------------------------")
    print(" ADD ACCOUNT FOR SUBJECT TEACHER ")
    print("---------------------------------")

    find_teacher_to_make_account = (sub_teacher_in_db.find_one({"FirstName": fn}) or
                                    sub_teacher_in_db.find_one({"ID": teacher_id}))

    if find_teacher_to_make_account:
        while True:
            username = input("Enter a username (must be at least 8 characters): ").upper().strip()
            find_username = ((students_enrolled.find_one({"Username": username}) or
                             irregular_student_enrolled.find_one({"Username": username})) or
                             teacher_in_db.find_one({"Username": username})) or sub_teacher_in_db.find_one({"Username": username})
            if len(username) <= 7:
                print("Username must be at least 8 characters long. Please try again.")
            elif find_username:
                print("Username already exist. Please try again.")
            else:
                while True:
                    password = input("Enter a Password (must be at least 6 characters long, include an uppercase letter, a lowercase letter, and a digit): ").strip()
                    find_password = (((students_enrolled.find_one({"Password": password}) or
                                       irregular_student_enrolled.find_one(
                                           {"Password": password})) or
                                      teacher_in_db.find_one({"Password": password})) or
                                     sub_teacher_in_db.find_one({"Password": password}))
                    if len(password) <= 5:
                        print("Password must be at least 6 characters long. Please try again.")
                    elif find_password:
                        print("Password already exists. Please try again.")
                    else:

                        upper = re.search(r'[A-Z]', password)
                        lower = re.search(r'[a-z]', password)
                        numbers = re.search(r'[0-10]', password)

                        if not upper:
                            print("Password must include an uppercase letter. Please try again.")
                        elif not lower:
                            print("Password must include a lower letter. Please try again.")
                        else:
                            if not numbers:
                                print("Password must include digits. Please try again")
                            else:
                                sub_teacher_in_db.update_one({"FirstName": fn},
                                                                      {"$set": {
                                                                          "Username": username,
                                                                          "Password": password}})
                                print("-------------------------")
                                num = 0
                                get_list= sub_teacher_in_db.find({})
                                for teach in get_list:
                                    num += 1
                                    print(f'{num}. First Name: | {teach.get("FirstName")} | Last Name: {teach.get("LastName")} | ID: {teach.get("ID")}')
                                print("-------------------------")

                                print(f"Teacher: {teacher_id} has been assigned")

                                while True:
                                    opt = input(
                                        "Do you want to add another subject teacher? (yes/no): ").lower().strip()
                                    if opt == "yes":
                                        add_sub_teacher()
                                        break
                                    elif opt == "no":
                                        admin_dashboard()
                                        break
                                    else:
                                        print("Invalid input. Please enter 'yes' or 'no'.")
                                break
                break

def login_student():
    if students_enrolled.count_documents({}) == 0:
        print("No student has been enrolled.")
        main_dashboard()
    else:
        print("--------------------")
        print("    LOGIN STUDENT   ")
        print("--------------------")
        print("")
        while True:
            username = input("Enter username: ").upper().strip()
            find_username = students_enrolled.find_one({"Username": username}) or irregular_student_enrolled.find_one({"Username": username})
            if find_username:
                while True:
                    student_id = input("Enter ID: ").upper().strip()
                    find_student_id = (students_enrolled.find_one({"Username": username, "ID": student_id}) or
                                       irregular_student_enrolled.find_one({"Username": username, "ID": student_id}))
                    if find_student_id:
                        while True:
                            password = input("Enter password: ")
                            find_student_password = (students_enrolled.find_one({"Username": username, "ID": student_id, "Password": password}) or
                                       irregular_student_enrolled.find_one({"Username": username, "ID": student_id, "Password": password}))
                            if find_student_password:
                                student_dashboard(username, student_id)
                                return username, student_id
                            else:
                                print("Incorrect password. Please try again.")
                    else:
                        print("Invalid student ID. Please try again.")
            else:
                print("The username entered is incorrect.")


def student_dashboard(username, student_id):
    print("Welcome to the Student Dashboard", username)
    print("--------------------------------")
    print("1. View Subjects and Grade")
    print("2. View Final Grade")
    print("3. View Profile")
    print("4. Logout") #goes back to main dashboard
    print("--------------------------------")
    print("")
    while True:
        choose = input("Enter an option: ").strip()
        if choose == "1":
            view_subject(username,student_id)
            break
        elif choose == "2":
            final_grade(username,student_id)
            break
        elif choose == "3":
            view_student_profile(username, student_id)
            break
        elif choose == "4":
            main_dashboard()
            break
        else:
            print("wrong")

def view_subject(username, student_id):
    student = (((students_enrolled.find_one({"Username": username}) or
               students_enrolled.find_one({"ID": student_id})) or
               irregular_student_enrolled.find_one({"Username": username})) or
               irregular_student_enrolled.find_one({"ID": student_id}))
    num = 0
    if student:
        print("Your Subjects and Grades")
        print("------------------------------------------------")
        for subjects, grades in student['Subjects'].items():
            num += 1
            print(f'{num}. Subject: {subjects} | Grades: {grades}')
        print("------------------------------------------------")

    student_dashboard(username, student_id)

def view_student_profile(username, student_id):
    student = (((students_enrolled.find_one({"Username": username}) or
                 students_enrolled.find_one({"ID": student_id})) or
                irregular_student_enrolled.find_one({"Username": username})) or
               irregular_student_enrolled.find_one({"ID": student_id}))
    if student:
        print("YOUR PROFILE")
        print("------------------------------------------------")
        print(f'First Name: {student.get("FirstName")}')
        print(f'Middle Name: {student.get("MiddleName")}')
        print(f'Last Name: {student.get("LastName")}')
        print(f'Birth Date: {student.get("BirthDate")}')
        print(f'Year: {student.get("Year Level")}')
        print(f'Sem: {student.get("Sem")}')
        print(f'Username: {student.get("Username")}')
        print(f'Password: {student.get("Password")}')
        print("------------------------------------------------")
        print("")
    student_dashboard(username, student_id)

def final_grade(username, student_id):
    student = (((students_enrolled.find_one({"Username": username}) or
                 students_enrolled.find_one({"ID": student_id})) or
                irregular_student_enrolled.find_one({"Username": username})) or
               irregular_student_enrolled.find_one({"ID": student_id}))

    if student:
        print("------------------------------------------------")
        print(f'Final Grade: {student.get("Final Grade")}')
        print("------------------------------------------------")
        print("")
    student_dashboard(username, student_id)

def login_sub_teacher():
    count_teacher = sub_teacher_in_db.count_documents({})
    if count_teacher <= 0:
        print("No teachers have been added yet.")
        main_dashboard()
    else:
        print("---------------------")
        print("    LOGIN TEACHER    ")
        print("---------------------")
        print("")
        while True:
            username = input("Enter username: ").upper().strip()
            find_teach_username = sub_teacher_in_db.find_one({"Username": username})
            if find_teach_username:
                while True:
                    teacher_id = input("Enter ID (6-digit ID): ").strip()
                    find_teach_id = sub_teacher_in_db.find_one({"Username": username, "ID": teacher_id})

                    letter1 = re.search(r'[a-z]', teacher_id)
                    letter2 = re.search(r'[A-Z]', teacher_id)

                    if letter1:
                        print("ID does not exist. Please try again.")
                    elif letter2:
                        print("ID does not exist. Please try again.")
                    else:
                        if find_teach_id:
                            while True:
                                password = input("Enter password: ").strip()
                                find_teach_pass = sub_teacher_in_db.find_one({"Username": username, "ID": teacher_id, "Password": password})

                                if find_teach_pass:
                                    print("")
                                    subject = find_teach_pass.get("Subject To Handle")
                                    sub_teacher_dashboard(username,teacher_id,subject)
                                    return username, teacher_id, subject
                                else:
                                    print("Password incorrect. Please try again.")


                        else:
                            print("ID does not exist. Please try again.")
            else:
                print("Username does not exist. Kindly re-enter the information.")

def sub_teacher_dashboard(username, teacher_id,subject):
    print("-------------------------")
    print("--  TEACHER DASHBOARD  --")
    print("-------------------------")
    print("")

    print("1. View Students")
    print("2. Search Student")
    print("3. Update Student Grade")
    print("4. View Students Grade")
    print("5. Logout")
    print("")
    while True:
        choice = input("Enter an option: ")

        if choice == "1":
            view_teacher_student(username, teacher_id,subject)
            break
        elif choice == "2":
            search_student(username, teacher_id,subject)
            break
        elif choice == "3":
            update_student_grade(username, teacher_id,subject)
            break
        elif choice == "4":
            view_students_grade(username, teacher_id,subject)
            break
        elif choice == "5":
            main_dashboard()
            break
        else:
            print("Option does not exist. Please try again")

def view_students_grade(username, teacher_id,subject):
    zero = sub_teacher_in_db.count_documents({"Students": []})
    if zero == 0:
        print("No students are enrolled to your subject")
        sub_teacher_dashboard(username, teacher_id, subject)
    else:
        print("Student Grade Summary: ")
        print("-------------------------------")
        students_of_teacher = students_enrolled.find({f"Subjects.{subject}": {"$exists": True}})
        irregular_students_of_teacher = irregular_student_enrolled.find({f"Subjects.{subject}": {"$exists": True}})
        mix = list(students_of_teacher) + list(irregular_students_of_teacher)
        num = 0
        for student in mix:
            num += 1
            grade = student.get('Subjects', {}).get(subject, None)
            if grade is not None:
                print(f"{num}. Last Name: {student['LastName']} | Student ID: {student['ID']} | Grade: {grade}")
            else:
                print(f"Student ID: {student['ID']}, No grade available for {subject}")

        sub_teacher_dashboard(username, teacher_id,subject)



def search_student(username, teacher_id,subject):
    print("-----------------------")
    print("    SEARCH STUDENT     ")
    print("-----------------------")
    print("")
    zero = sub_teacher_in_db.count_documents({"Students": []})
    if zero == 0:
        print("No students are enrolled to your subject")
        sub_teacher_dashboard(username, teacher_id,subject)
    else:
        print("-------------------------------------------------------------------------")
        students = sub_teacher_in_db.find({"Username": username, "ID": teacher_id})
        num = 0
        for document in students:  # Iterate over the documents matching the query
            if 'Students' in document:  # Check if 'Students' field is in the document
                for student in document['Students']:  # Iterate over each student in the 'Students' array
                    num += 1
                    print(
                        f'{num}. Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
        print("-------------------------------------------------------------------------")
        while True:
            find_ln = input("Enter last name of student: ").upper().strip()
            if students_enrolled.find_one({"LastName": find_ln}) or irregular_student_enrolled.find_one({"LastName": find_ln}):
                while True:
                    find_id = input("Enter ID of student: ").strip()
                    if students_enrolled.find_one({"LastName": find_ln, "ID": find_id}) or irregular_student_enrolled.find_one(
                        {"LastName": find_ln, "ID": find_id}):

                        find_student = students_enrolled.find_one({"LastName": find_ln, "ID": find_id}) or irregular_student_enrolled.find_one({"LastName": find_ln, "ID": find_id})
                        if find_student:
                            print("")
                            print("--------------------------------------------------")
                            print("First Name:", find_student.get("FirstName"))
                            print("Middle Name:", find_student.get("MiddleName"))
                            print("Last Name:", find_student.get("LastName"))
                            print("Birth Date:", find_student.get("BirthDate"))
                            print("Year:", find_student.get("Year Level"))
                            print("Sem:", find_student.get("Sem"))
                            print("Username:", find_student.get("Username"))
                            print("--------------------------------------------------")

                            sub_teacher_dashboard(username, teacher_id, subject)

                        else:
                            print("No student exists. Please try again.")
                    else:
                        print("No ID exist. Please try again.")
            else:
                print("No student exists. Kindly re-enter the information.")

def view_teacher_student(username, teacher_id, subject):
    zero = sub_teacher_in_db.count_documents({"Students": []})
    if zero == 0:
        print("No students are enrolled to your subject")
        sub_teacher_dashboard(username, teacher_id, subject)
    else:
        print("-----------------------")
        print("     YOUR STUDENTS     ")
        print("-----------------------")
        print("")
        print("-------------------------------------------------------------------------")
        students = sub_teacher_in_db.find({"Username": username, "ID": teacher_id})
        num = 0
        for document in students:  # Iterate over the documents matching the query
            if 'Students' in document:  # Check if 'Students' field is in the document
                for student in document['Students']:  # Iterate over each student in the 'Students' array
                    num += 1
                    print(f'{num}. First Name: {student.get("FirstName")} | Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
        print("-------------------------------------------------------------------------")

        sub_teacher_dashboard(username, teacher_id, subject)

def update_student_grade(username,teacher_id, subject):
    zero = sub_teacher_in_db.count_documents({"Students": []})
    if zero == 0:
        print("No students are enrolled to your subject")
        sub_teacher_dashboard(username, teacher_id, subject)
    else:
        print("-----------------------")
        print("       GIVE GRADE      ")
        print("-----------------------")
        print("")
        print("-------------------------------------------------------------------------")
        students = sub_teacher_in_db.find({"Username": username, "ID": teacher_id})
        num = 0
        for document in students:  # Iterate over the documents matching the query
            if 'Students' in document:  # Check if 'Students' field is in the document
                for student in document['Students']:  # Iterate over each student in the 'Students' array
                    num += 1
                    print(
                        f'{num}. Last Name: {student.get("LastName")} | ID: {student.get("ID")}')
        print("-------------------------------------------------------------------------")

        while True:
            find_ln = input("Enter last name of student: ").upper().strip()
            if students_enrolled.find_one({"LastName": find_ln}) or irregular_student_enrolled.find_one(
                    {"LastName": find_ln}):
                while True:
                    find_id = input("Enter ID of student: ").strip()
                    if students_enrolled.find_one({"LastName": find_ln, "ID": find_id}) or irregular_student_enrolled.find_one(
                            {"LastName": find_ln, "ID": find_id}):

                        find_student = students_enrolled.find_one({"LastName": find_ln, "ID": find_id}) or irregular_student_enrolled.find_one(
                            {"LastName": find_ln, "ID": find_id})


                        if find_student:
                            while True:
                                new_grade = float(input(f"Enter student's grade for the subject '{subject}' (0-100): "))
                                # Update the specific subject grade in the 'Subjects' object
                                if new_grade <= 100.0:
                                    students_enrolled.update_one(
                                        {"ID": find_id, "LastName": find_ln},
                                        {"$set": {f"Subjects.{subject}": new_grade}}
                                    )

                                    irregular_student_enrolled.update_one(
                                        {"ID": find_id, "LastName": find_ln},
                                        {"$set": {f"Subjects.{subject}": new_grade}}
                                    )

                                    print("Student grade has been updated")
                                    sub_teacher_dashboard(username, teacher_id, subject)

                                else:
                                    print("Invalid Entry: Grades cannot exceed 100. Please enter a valid grade")
                        else:
                            print("No student exists. Please try again.")
                    else:
                        print("Invalid student ID. Kindly re-enter the information")
            else:
                print("Student Not Found")


main_dashboard()

client.close()