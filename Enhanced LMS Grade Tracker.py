print("=" * 28)
print(" ENHANCED LMS GRADE TRACKER ")
print("=" * 28)

#Student ID Validation
StuIdValid = False
while not StuIdValid:
    StuId = input("Enter your Student ID: ")
    if StuId.isdigit():
        if int(StuId) > 0:
            StuIdValid = True
        elif int(StuId) <= 0:
            print("The Student ID needs to be non-zero and positive.")
        else:
            print("Invalid")
    else:
        print("The Student ID needs to be only digits.")
FormStuID = "STU" + StuId.zfill(5)

#Student Name Validation
Name = input("Enter your Full Name: ")
while not True:
    if Name.isalpha() and len(Name) >= 3:
        Name = Name.strip().title()
        print(f"Welcome, {Name}")
    else:
        print("Invalid Name")

#Email Creation
First_N = Name.split()[0].lower()
Email = f"{First_N}.{StuId}@university.edu"

print("                  FEE - DETAILS                  ")
#Course Fee
BCF = int(input("Enter your Base Course Fee: "))
Description = input("Enter Student Description: ").lower()
DesDisc = 0
if "reference" in Description:
    DesDisc += 5000
elif "scholarship" in Description:
    DesDisc += 7000
elif "promo" in Description:
    DesDisc += 3000

Final_Fee = BCF - DesDisc

#Student Grade Tracker
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
print(f"Student ID: {FormStuID}")
print(f"Student Name: {Name.upper()}")
print(f"Your Student Unique Email: {Email}")
print(f"Student Attendance: {ATD}%")
print(f"Total Score: {TScore}")
print(f"Total Number of Subjects: {Subject}")
print(f"Average Score: {round(float(Avg_Score),1)}")
print(f"Performance: {PStatus}")
print(f"Attendance Status: {AStatus}")
print(f"Base Course Fee: {BCF}")
print(f"You Got Discount: {DesDisc} ")
print(f"After Discount Pay: {Final_Fee}")
print("\n ================= ================= \n")