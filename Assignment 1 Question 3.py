# Part 3: Display Loan Information

# Your function for calculating payment goes here
def get_monthly_payments(principle, annual_interest_rate, duration):
    r = annual_interest_rate / 100 / 12 # monthly rate
    n = duration * 12 # number of months
    if (annual_interest_rate == 0):
        monthly_payment = principle / n
    else:
        monthly_payment = principle*(r*(1+r)**n)  / ((1+r)**n - 1)        
    return monthly_payment

# Your function for calculating remaining balance goes here
def get_remaining_loan_balance(principle, annual_interest_rate, duration, number_of_payments):
    r = annual_interest_rate / 100 / 12 # monthly rate
    n = duration * 12 # number of months
    p = number_of_payments #number of monthly payments that are already paid.
    if (annual_interest_rate == 0):
        remaining_loan_balance = principle*(1 - (p/n))
    else:
        remaining_loan_balance = principle*((1+r)**n - (1+r)**p)  / ((1+r)**n - 1)        
    return remaining_loan_balance

# Your main program goes here
principle=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

monthly_payment = get_monthly_payments(principle, annual_interest_rate, duration)

print("LOAN AMOUNT:", principle, "INTEREST RATE (PERCENT):", annual_interest_rate)
print("DURATION (YEARS):", duration, "MONTHLY PAYMENT:", int(monthly_payment))

for x in range(1,duration+1):
    number_of_payments = x * 12    
    remaining_balance = get_remaining_loan_balance(principle, annual_interest_rate, duration, number_of_payments)
    total_payment = monthly_payment * number_of_payments
    print("YEAR:", x, "BALANCE:", int(remaining_balance),"TOTAL PAYMENT", int(total_payment))
