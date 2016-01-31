# Ask the user to enter a positive integer, seconds
user_response = input("Please enter an integer, seconds: ")
s = int(user_response)

# Output time stats
days = s / 60 / 60 / 24
hours = (s / 60 / 60) % 24
minutes = (s / 60) % 60
seconds = s % 60
print(int(days), "days", int(hours), "hours", int(minutes), "minutes", int(seconds), "seconds")
