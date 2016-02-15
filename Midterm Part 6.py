# Accepts a list as parameter and returns a boolean
# based on whether or not the list is the same forward and backwards.
def crazy_list(some_list):
    for i in range(len(some_list)//2):
         if some_list[i] != some_list[-1-i]:
                 return False
    return True

