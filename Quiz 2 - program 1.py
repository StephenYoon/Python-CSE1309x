# Asks the user to enter their age in years
# Assume that the user always enters an integer
user_response = input("Please enter your age in years: ")
age_in_years = int(user_response) # or float(user_response)

# Print the appropriate output based on requirements
if (age_in_years <= 0):
    print("UNBORN")
elif (age_in_years > 0 and age_in_years <= 150):
    print("ALIVE")
else:
    print("VAMPIRE")
