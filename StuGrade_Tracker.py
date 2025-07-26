
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