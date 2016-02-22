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

        if(length1 < length2):
            shortest_length = length1
            shortest_word = s1_list
            longest_word = s2_list
        else:
            shortest_length = length2
            shortest_word = s2_list
            longest_word = s1_list

        #print('Past 1', ''.join(shortest_word), ''.join(longest_word))
        # find 1 mismatch character and remove it
        for i in range(0, shortest_length):
            if(shortest_word[i] != longest_word[i]):
                longest_word.remove(longest_word[i])
                break
            
        #print('Past 2', ''.join(shortest_word), ''.join(longest_word))
        # if the arrays are the same, then we are good, else not good
        for i in range(0, shortest_length):
            if(shortest_word[i] != longest_word[i]):
                can_be_fixed = False
                break
            
        if (can_be_fixed):
            return 1
        else:
            return 2

    # Leftover scenario, return 2
    else:
        return 2