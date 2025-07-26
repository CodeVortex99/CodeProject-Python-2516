# Requirements: Principal Loan Amount, monthly Rate of Interest, Tenure of the loan in months

print("Welcome to the EMI Calculator")

print("\n Menu:")
print("1. Principal Loan Amount")
print("2. Down Payment")
Choice = int(input("Enter your choice: "))

if Choice == 1:
    PLA = float(input("Enter the principal loan amount: "))
elif Choice == 2:
    TA = float(input("Enter the total amount:: "))
    DP = float(input("Enter the down payment: "))
    PLA = TA - DP
else:
    try:
        Choice = int(input("Enter your choice: "))
    except:
        print("You have to choose between option 1 or 2.")

print("\n interest rate menu: ")
print("1. Monthly Interest Rate")
print("2. Annual Interest Rate")
Choice_1= int(input("Enter your choice: "))

if Choice_1 == 1:
    RI = float(input("Enter the monthly rate of interest: "))
elif Choice_1 == 2:
    YI = float(input("Enter the annual rate of interest: "))
    RI = YI / 1200
else:
    try:
        Choice_1 = int(input("Enter your choice: "))
    except:
        print("You have to choose between option 1 or 2.")

print("\n Tenure menu: ")
print("1. Monthly Tenure")
print("2. Annual Tenure")
Choice_2 = int(input("Enter your choice: "))

if Choice_2 == 1:
    MI = float(input("Enter the tenure of the loan in months: "))
elif Choice_2 == 2:
    YI = float(input("Enter the tenure of the loan in years: "))
    MI = YI * 12
else:
    try:
        Choice_2 = int(input("Enter your choice: "))
    except:
        print("You have to choose between option 1 or 2.")

EMI = (PLA * RI * (1 + RI) ** MI) / ((1 + RI) ** MI - 1)

print(f"The EMI is: {EMI}")