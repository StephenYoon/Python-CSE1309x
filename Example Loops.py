# Samples: for and while loops
for current_number in range(1,11): # up to range -1
	print("Iteration ", current_number)

for x in ["Ford", "Nissan", "Mercedes", "Audi", "Hyundai"]:
	print("Car ", x)
	
x = 0
while (x < 10):
        print("Index ", x)
        x = x + 1

# Samples: continue and break
count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
print(count)

k = 1
while k<5:
    if k % 7 == 0:
        break
    k = k + 2
print(k)

my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    if element == "cat":
        continue
    count = count + 1
print(count)

my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)
