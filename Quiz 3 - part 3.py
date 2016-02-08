number = int(input("Enter a positive number >= 3"))

for z in range(1,number+1):
    stars = ""
    for p in range(1,z+1):
        stars = stars + "*"
    print(stars)
            
for z in range(number, 1, -1):
    stars = ""
    for p in range(1,z):
        stars = stars + "*"
    print(stars)
