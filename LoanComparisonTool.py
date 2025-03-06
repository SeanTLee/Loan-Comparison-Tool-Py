import math

def calculate_loan_details(principal, annual_rate, years):
    """
    Calculates the monthly payment and total interest paid for a given loan.
    """
    monthly_rate = (annual_rate / 100) / 12
    months = years * 12
    
    if monthly_rate == 0:
        monthly_payment = principal / months
    else:
        monthly_payment = (principal * monthly_rate) / (1 - math.pow(1 + monthly_rate, -months))
    
    total_payment = monthly_payment * months
    total_interest = total_payment - principal
    
    return round(monthly_payment, 2), round(total_interest, 2)

def compare_loans(loan_options, tenure):
    """
    Compares multiple loan options based on the user-inputted tenure and prints the details.
    """
    print("\nLoan Comparison:")
    print("-----------------------------------------------------------")
    print("Loan Type | Loan Amount | Interest Rate | Monthly Payment | Total Interest Paid")
    print("-----------------------------------------------------------------------------------")
    
    for loan in loan_options:
        loan_type, principal, annual_rate = loan
        monthly_payment, total_interest = calculate_loan_details(principal, annual_rate, tenure)
        print(f"{loan_type:10} | ${principal:10} | {annual_rate:13}% | ${monthly_payment:14} | ${total_interest:19}")

# Input loan details
loan_options = []
n = int(input("Enter the number of loan types to compare: "))
tenure = int(input("Enter the loan tenure in years: "))

for _ in range(n):
    loan_type = input("Enter loan type (e.g., Home, Car, Personal): ")
    principal = float(input(f"Enter loan amount for {loan_type}: "))
    annual_rate = float(input(f"Enter interest rate for {loan_type} (%): "))
    loan_options.append((loan_type, principal, annual_rate))

compare_loans(loan_options, tenure)
