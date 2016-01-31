# Asks the user to enter a integer, total number hours worked in a week.
# Any number less than 0 or greater than 168 (n < 0 or n > 168), print INVALID 

# Assume that hourly rate for the first 40 hours is $8 per hour.
# Hourly rate for extra hours between 41 and 50 (41 <= n < 50 ) is $9 per hour.
# Hourly rate for extra hours greater than or equal to 50 is $10 per hour.

user_response = input("Please enter an integer: ")
n = int(user_response)
rate = 8
rate2 = 9
rate3 = 10

# Print the appropriate output based on requirements
if (n < 0 or n > 168): #for example 12
    print("INVALID")
elif (n <= 40):
    dollars = n * rate
    print("YOU MADE", dollars, "DOLLARS THIS WEEK")
elif (n < 50):
    reg_pay = 40 * rate
    big_pay = (n-40) * rate2
    total_dollars = reg_pay + big_pay
    print("YOU MADE", total_dollars, "DOLLARS THIS WEEK")
else:
    reg_pay = 40 * rate # $320, first 40 hours
    big_pay = (10) * rate2 # 81, n < 50, next 9 hours up to 49 hours
    wow_pay = (n-49) * rate3 #, remaining hours get $10 rate
    total_dollars = reg_pay + big_pay + wow_pay
    print("YOU MADE", total_dollars, "DOLLARS THIS WEEK")
