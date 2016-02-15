# Accepts a list of integers
# Returns the integer from the list that has the most divisors
def find_integer_with_most_divisors (input_list):

    # trackers for winning integer
    max_divisors = 0
    winning_integer = None
    
    # iterate for each integer value
    for orig_value in input_list:

        value = int(abs(orig_value))

        # determine number of divisors
        divisors = 0
        for i in range(1, value+1):
            if (value == 0):
                continue
            
            if (value%i) == 0:
                divisors = divisors + 1

        # check to see if this integer has the most divisors
        if (divisors > max_divisors):
            max_divisors = divisors
            winning_integer = orig_value
        
    # return winning integer
    return winning_integer
