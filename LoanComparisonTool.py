from flask import Flask, render_template, request
import math

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        n = int(request.form['loan_count'])
        tenure = int(request.form['tenure'])
        
        loan_options = []
        for i in range(n):
            loan_type = request.form[f'loan_type_{i}']
            principal = float(request.form[f'principal_{i}'])
            annual_rate = float(request.form[f'annual_rate_{i}'])
            loan_options.append((loan_type, principal, annual_rate))

        # Calculate loan details
        loan_details = []
        total_loan_amount = 0
        total_interest_paid = 0

        for loan in loan_options:
            loan_type, principal, annual_rate = loan
            monthly_payment, total_interest = calculate_loan_details(principal, annual_rate, tenure)
            loan_details.append({
                'loan_type': loan_type,
                'principal': principal,
                'annual_rate': annual_rate,
                'monthly_payment': monthly_payment,
                'total_interest': total_interest
            })
            total_loan_amount += principal
            total_interest_paid += total_interest
        
        return render_template('results.html', loan_details=loan_details, total_loan_amount=total_loan_amount, total_interest_paid=total_interest_paid)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
