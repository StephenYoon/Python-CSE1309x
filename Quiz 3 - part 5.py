# returns True if the integer is a perfect number
def is_perfect_number(number):
    total_sum = 0
    for x in range(1,number):
        if (number%x == 0):
            total_sum += x
    return total_sum == number
