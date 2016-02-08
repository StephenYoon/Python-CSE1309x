# Part 1: Calculate Monthly payments for a loan
def get_monthly_payments(principal, annual_interest_rate, duration):
    
    r = annual_interest_rate / 100 / 12 # monthly rate
    n = duration * 12 # number of months
    
    if (annual_interest_rate == 0):
        monthly_payment = principal / n
    else:
        monthly_payment = principal*(r*(1+r)**n)  / ((1+r)**n - 1)
    
    return monthly_payment


