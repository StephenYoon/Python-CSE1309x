# Type your code here
user_response = input("Please enter an integer between 1 and 7: ")
day_index = int(user_response)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

if day_index >= 1 and day_index <= 7:
    print(days[day_index - 1])
else:
    print("Number not between 1 and 7.")
