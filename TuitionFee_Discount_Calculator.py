Name = input("Enter your name: ")
Grade = int(input("Enter you level between 1 to 12: "))
B_TuitionFee = float(input("Enter your tuition fee: "))
Discount = 0 #float(input("Enter your discount percentage: "))
ATS = input("Are you an academic topper? (yes/no): ")

if 1 <= Grade <= 12:
    if 9 <= Grade <= 12:
        if ATS == "yes":
            Discount = 0.2
        else:
            Discount = 0.1
    elif 6 <= Grade <= 8:
        Discount = 0.05
    elif Grade < 6:
        Discount = 0
else:
    print("Invalid Grade")
    try:
        Grade = int(input("Enter your level between 1 to 12: "))
    except:
        print("Please enter a valid grade.")

match Grade:
    case 10:
        Discount += 0.03
    case 12:
        Discount += 0.05

Final_Discount = Discount * 100
Final_TuitionFee = (1 - Discount) * B_TuitionFee

#Output
print("\n--------------------------------------------------------------\n")
print(f"Name: {Name.upper()}")
print(f"Grade Level: {Grade}")
print(f"Academic Topper: {ATS.upper()}")
print(f"Base Tuition Fee: {B_TuitionFee} Rupees")
print(f"Total Discount Percentage: {Final_Discount}%")
print(f"Total Discount Amount: {B_TuitionFee - Final_TuitionFee} Rupees")
print(f"Final Tuition Fee: {Final_TuitionFee} Rupees")