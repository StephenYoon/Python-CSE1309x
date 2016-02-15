# Pattern Sum
def pattern_sum(a, b):
    values = []
    for i in range(1, b+1):
        value = ""
        for i in range(1,i+1):
            value = value + str(a)
        values.append(int(value))

    return sum(values)
    
print(pattern_sum(4,5))
