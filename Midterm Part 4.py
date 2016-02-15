# returns True if the number is a prime number
def is_prime_number(x):
        if x >= 2:
            for y in range(2,x):
                if not ( x % y ):
                    return False
        else:
            return False
        return True

# accepts a positive integer n
# returns a sorted list (ascending order) of all the prime numbers between 2 and n
# (including 2 but not including n)
def list_of_primes(n):
    prime_list = []
    for x in range(2, n):
        if(is_prime_number(x)):
            prime_list.append(x)

    return prime_list

print(list_of_primes(29))
