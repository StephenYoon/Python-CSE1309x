# Return the sum of all the odd numbers in the list
def sum_odd_numbers(numbers):
    total_sum = 0
    for x in numbers:
        if (x%2 == 1):
            total_sum += x

    return total_sum
