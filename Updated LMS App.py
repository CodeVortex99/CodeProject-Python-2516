
import sys
# LMS -> Sub Feature - Student Management System
# System Information --> Tuples
SYSTEM_INFO = ("LMS Students Portal","v1.0","2025","Edify University")
ADMIN_INFO = ("admmin@edify.ai","9876543210","201")

# display system info
print("="*50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Developed By {SYSTEM_INFO[3]}")
print("="*50)

Students = {}

def main():
    print("\nChoose an option from (1-5): \n")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. List All Students")
    print("5. Search")
    print("6. Exit System")
    global Choice
    Choice = input("\nEnter your choice: ")

def Add_Student():
    Stud_ID = input("Enter your student ID: ")
    if Stud_ID in Students:
        print("Student Already Exists with this ID.")
    else:
        Name = input("\nEnter your name: ").title()
        Scores = input("\nEnter your Scores seperated by a ',': ").split(',')
        Skills = set(input("\nEnter your Skills Set seperated by ',': ").split(','))

        Students[Stud_ID] = {"Name": Name, "Scores": Scores, "Skills": Skills}
        print("\nStudent Successfully Added to the Applicaiton.") 
    main()

def Update_Student():
    Stud_ID = input("Enter your student ID: ")
    if Stud_ID in Students:
        Name = input("Enter your name: ").title()
        Students[Stud_ID]["Name"] = Name
        print("Updated the Name succesfully.")
    else:
        print("Student Doesn't exist.")
    main()
    
def Delete_Student():
    Stud_ID = input("Enter your student ID: ")
    Removed = Students.pop(f"{Stud_ID}", None)
    print("Student Successfully Deleted") if Removed else print("Student Doesn't exist to be deleted.")
    
    main()
    
def List_Students():
    for i in Students:
        if not Students:
            print("No Students Available")
        else:
            for key, value in Students[i].items():
                print("="*20)
                print(f"ID: {key}")
                print(f"    Name: {value[0]}")
                print(f"    Scores: {value[1]}")
                print(f"    Skills: {value[2]}")
    main()

def Search():
    Stud_ID = input("Enter your student ID: ")
    if Stud_ID in Students:
        for values in Students[Stud_ID]:
            for key, value in values.items():
                print(f"{key}: {value}\n")

match Choice:
    case 1:
        print("\n... Action 1 taking place ...\n")
        Add_Student()
    case 2:
        print("\n... Action 2 taking place ...\n")
        Update_Student()
    case 3:
        print("\n... Action 3 taking place ...\n")
        Delete_Student()
    case 4:
        print("\n... Action 4 taking place ...\n")
        List_Students()
    case 5:
        print("\n... Action 5 taking place ...\n")
        Search()
    case 6:
        print("Thank you for using the application.")
        print("\n... Exiting the system ...")
        sys.exit()