# Assessment Task: Tuition Discount Calculation in Python

# Task Requirements:
    # Variables:
    # Get user input for the following information:
    # Student's name 
    # Student's grade level (1-12) 
    # Base tuition fee 
    # Discount percentage 
    # Academic Topper status (e.g., whether the student is an academic topper or not)

# Input Validation
    # Implement input validation using conditional statements
    # Check if grade is between 1-12
    # Display appropriate error message for invalid grades
    # Process discount calculation only for valid input
# Conditional Statements for Discount Calculation:
    # Use Conditional statements to determine the discount based on the following rules:
    # For students in grades 9 to 12:
    # If they are academic toppers, apply a 20% discount.
    # Otherwise, apply a 10% discount.
    # For students in grades 6 to 8, apply a 5% discount.
    # For grades below 6, apply no discount.

# Implement match-case Statement for Additional Discounts:
    # Implement a match-case statement to apply additional discounts:
    # For grade 10, add an additional 3% discount.
    # For grade 12, add an additional 5% discount.
    # No additional discounts for other grades.
# Calculation:
    # Calculate the final tuition fee after applying the discount:
    # Calculate discount amount
    # Calculate final fee
# Output:
    # Display a detailed summary including
        # Student name
        # Grade level
        # Academic topper status (Yes/No)
        # Base tuition fee
        # Total discount percentage
        # Discount amount saved
        # Final tuition fee after discount

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