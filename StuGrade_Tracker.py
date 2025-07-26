# Assessment Task: Student Grade Tracker
    # Collect Student Information:
    # Student ID 
    # Student Name 
    # Attendance 
    # Number of subjects
    # Total Score 
    # Continue input

    # Input Subject Scores:
        # Repeatedly ask the user to enter scores for multiple subjects.
        # Accepts "yes" or "Yes" as continuation options
        # Add each entered score to the total score and increment the number of subjects.
        # Continuation prompt: Ask the user if they want to enter another score after each entry (allowing them to continue or stop inputting scores).
    # Calculate Average Score:
        # Calculate the average score for the student after all scores are entered.
    # Determine Performance Level:
        # Use conditional statements to determine performance based on the average score:
        # 85 and above → "Excellent"
        # 70 to 84 → "Good"
        # 50 to 69 → "Average"
        # Below 50 → "Needs Improvement"

    # Check Attendance Status:
        # Use a conditional statement to check if attendance is less than 75%. If so, print a WARNING Low Attendance, else OK Attendance Satisfied

    # Display Final Results:
        # Print out the student’s ID, name, total score, average score, performance level, and attendance with appropriate messages.

ID = int(input("\nEnter Your ID: "))
Name = input("Enter Your Name: ")
ATD = float(input("What is your attendance: "))

TScore = 0
Subject = 0

while True:
    Subject += 1
    Score = int(input(f"\nEnter Score for Subject {Subject}: "))
    TScore += Score
    Ask = input("Do you want to enter another score? (yes/no): ")
    if Ask.lower() == "no":
        break

Avg_Score = TScore / Subject

PStatus = ""
if Avg_Score >= 85:
    PStatus = "Excellent"
elif 70 <= Avg_Score < 85:
    PStatus = "Good"
elif 50 <= Avg_Score < 70:
    PStatus = "Average"
elif Avg_Score < 50:
    PStatus = "Needs Improvement"

AStatus = ""
if ATD >= 75.0:
    AStatus = "OK, Attendance Satisfied"
elif ATD < 75.0:
    AStatus = "WARNING - Low Attendance"

print("\n ========= Student Details ========= \n")
print(f"Student ID: {ID}")
print(f"Student Name: {Name.upper()}")
print(f"Student Attendance: {ATD}%")
print(f"Total Score: {TScore}")
print(f"Total Number of Subjects: {Subject}")
print(f"Average Score: {round(float(Avg_Score),1)}")
print(f"Performance: {PStatus}")
print(f"Attendance Status: {AStatus}")
print("\n ================= ================= \n")