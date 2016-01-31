# Asks the user to enter a positive integer
# Assume that the user always enters an integer
user_response = input("Please enter an integer: ")
n = int(user_response)

# Print the appropriate output based on requirements
if (n%2==0 and n%3==0): #for example 12
    print("BOTH")
elif (n%2==0 or n%3==0): #for example 9
    print("ONE")
elif (not(n%2==0) and not(n%3==0)): #for example 25
    print("NEITHER")
