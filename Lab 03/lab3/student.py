# Hadi Hassan
# EPPS 6317

""".

Lab 03 - Student Gradebook

This programs stores student names and grades in a list.
The user can display the gradebook, add students,
remove students, modify student information,
and display the highest and lowest grades.
"""

menu = ""
print("What would you like to do?")
print("\t[1] Show full gradebook")
print("\t[2] Add Student")
print("\t[3] Remove Student")
print("\t[4] Modify Student Information")
print("\t[5] Display Highest Grade")
print("\t[6] Display Lowest Grade")
print("\t[7] Quit")

# Create an empty list to store each student's name and grade
student = []

# Keep the program running until the user chooses option 7
while menu != 7:
    # Try to convert the users input choice into an integer
    try:
        menu = int(input("Enter selection [1-7]"))
    # If the user enters something that is not in the value,
    # prevent it from crashing
    except ValueError:
        print("INVALID SELECTION, enter a number from 1 to 7.")
        continue
    # Reject numbers that are outsidfe the value range
    if menu > 7 or menu < 1:
        print("INVALID SELECTION, enter a number from 1 to 7")
        continue
    menu = int(input("Enter selection [1-7]"))
    # we want to see the list of all the Names and Grades
    if menu == 1:
        print("Name\tGrade")

        # Go through each student record one at a time
        for s in student:
            print(s[0] + "\t" + str(s[1]))

    # Ask the user to enter the name and grade of the student
    elif menu == 2:
        sname = input("Student Name?")
        sgrade = int(input("Student Grade?"))

        # Store the name and the grade of the student as one record
        student.append([sname, sgrade])

    # Search for the student by name and only remove that student record
    elif menu == 3:
        remove_name = input("Student Name to remove?")

        # Start by assuming that the student has not been found
        found = False

        # Search through each student in the gradebook
        for s in student:
            if s[0] == remove_name:
                found = True
                student.remove(s)

                # Stop search once the matching student has been removed
                break
        # If no student was found, tell the user student not found
        if not found:
            print("Student Not Found.")

    # Find a specific student and allow their name and/or grade to be changed
    elif menu == 4:
        modify_name = input("Student Name to modify?")
        found = False

        for s in student:
            if s[0] == modify_name:
                found = True
                new_name = input(
                    "New Student Name? (Press Enter to keep current name)"
                    )
                new_grade = input(
                    "New Student Grade? (Press Enter to keep current grade)"
                    )

                # Only replace the name if the user entered a new one
                if new_name != "":
                    s[0] = new_name

                # Only replace the grade if the user entered a new one
                if new_grade != "":
                    s[1] = int(new_grade)
                break
        if not found:
            print("Student Not Found.")

    # Check if the gradebook is empty before looking for the highest grade
    elif menu == 5:
        if len(student) == 0:
            print("No Student in the Gradebook")
        else:
            highest = student[0]

            # Compare every students grade with the highest grade found so far
            for s in student:
                if s[1] > highest[1]:
                    highest = s

            # Print the student with the highest grade
            print(highest[0] + "\t" + str(highest[1]))

    # Option 6 uses the same logic as Option 5, but finds the lowest grade
    elif menu == 6:
        if len(student) == 0:
            print("No student in the Gradebook")
        # Use the first student as the starting lowest grade
        else:
            lowest = student[0]
            # Compare every students grade with the lowest grade found so far
            for s in student:
                if s[1] < lowest[1]:
                    lowest = s
            # Print the student with the lowest grade
            print(lowest[0] + "\t" + str(lowest[1]))

print("Terminating program... Goodbye!")
