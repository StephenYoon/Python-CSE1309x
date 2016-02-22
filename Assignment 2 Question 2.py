# compare two strings
# return •0 if the two strings match exactly.
# return •1 if the first string can become the same as the second by inserting or deleting a single character.
# return •2 otherwise
def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    length1 = len(s1)
    length2 = len(s2)

    # same length, potential match
    if (s1 == s2):
        return 0

    # potential match by inserting/deleting 1 character
    elif (abs(length1 - length2) == 1):
        can_be_fixed = True
        s1_list = sorted(list(s1))
        s2_list = sorted(list(s2))
        shortest_length = length1 if length1 < length2 else length2

        # find 1 mismatch character and remove it
        for i in range(0, shortest_length):
            if(s1_list[i] != s2_list[i]):
                s2_list.remove(s2_list[i])
                break

        # if the arrays are the same, then we are good, else not good
        for i in range(0, shortest_length):
            if(s1_list[i] != s2_list[i]):
                can_be_fixed = False
                break
            
        if (can_be_fixed):
            return 1
        else:
            return 2

    # Leftover scenario, return 2
    else:
        return 2
        
##print(single_insert_or_delete('Python','Java'))
##print(single_insert_or_delete('book','boo'))
##print(single_insert_or_delete('sin','sink'))
##print(single_insert_or_delete('dog','Dog'))
##print(single_insert_or_delete('poke','spoke'))
##print(single_insert_or_delete('poker','poke'))
##print(single_insert_or_delete('programing','programming'))
