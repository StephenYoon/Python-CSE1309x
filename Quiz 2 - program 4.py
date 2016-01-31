# Ask the user to enter a positive integer, seconds
user_response = input("Please enter an integer, seconds: ")
s = int(user_response)

# Output time stats
days = s / 60 / 60 / 24
hours = (days - int(days)) * 24
minutes = (hours - int(hours)) * 60
seconds = (minutes - int(minutes)) * 60
print(int(days), "days", int(hours), "hours", int(minutes), "minutes", int(seconds), "seconds")
