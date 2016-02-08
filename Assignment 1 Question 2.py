# Part 2: Calculate the remaining balance of a loan
def get_remaining_loan_balance(principal, annual_interest_rate, duration, number_of_payments):
    
    r = annual_interest_rate / 100 / 12 # monthly rate
    n = duration * 12 # number of months
    p = number_of_payments #number of monthly payments that are already paid.
    
    if (annual_interest_rate == 0):
        remaining_loan_balance = principal*(1 - (p/n))
    else:
        remaining_loan_balance = principal*((1+r)**n - (1+r)**p)  / ((1+r)**n - 1)
    
    return remaining_loan_balance

