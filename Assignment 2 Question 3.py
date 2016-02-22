# first argument is a sentence (string)
# second argument is a list of words (correct_spells)
# •Do not spell check one or two letter words (copy them directly to the output string).
# •In case of a tie use the first word from the correct_spelled list
# •Ignore capitalization
# •All characters in the output string should all be in lower case letters
# •Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
# •Remove extra spaces between the words.
# •Remove spaces at the start and end of the output string.

def find_mismatch(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    length1 = len(s1)
    length2 = len(s2)

    # same length, potential match
    if (s1 == s2):
        return 0
    elif (length1 == length2):
        s1_list = list(s1)
        s2_list = list(s2)
        error_count = 0
        for i in range(0, length1):
            if(s1_list[i] != s2_list[i]):
                error_count = error_count + 1

        if (error_count == 1):
            return 1
        else:
            return 2
    else:
        return 2
    
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
        s1_list = list(s1)#sorted(list(s1))
        s2_list = list(s2)#sorted(list(s2))

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

# the goods
def spelling_corrector(s1,s2):
    words = s1.lower().strip().split() # remove leading/trailing/extra spaces
    correct_spells = []
    for correct_word in s2:
        correct_spells.append(correct_word.lower())

    final_words = []
    for word in words:
        
        # skip these words
        if (len(word) <= 2):
            #print('adding (skip):', word)
            final_words.append(word)
            continue        
        
        # if there is an exact match, add the word and move along
        exact_match = word in correct_spells
        if(exact_match):
            #print('adding (exact_match):', word, correct_word)
            final_words.append(word)
            continue

        # check to see if there is a replacement word (same length word)
        is_fixed = False
        for correct_word in correct_spells:
            result = find_mismatch(word, correct_word)
            if (result == 1):
                #print('adding (replacement):', word, correct_word)
                final_words.append(correct_word)
                is_fixed = True
                break
            
            result = single_insert_or_delete(word, correct_word)
            if (result == 1):
                #print('adding (insert/delete):', word, correct_word)
                final_words.append(correct_word)
                is_fixed = True
                break

        if (is_fixed):
            continue

        # no word replacement was found, add original word
        #print('adding (no fix):', word)
        final_words.append(word)        
        
    # Final output
    return ' '.join(final_words)#.lower()

# you are doing great
print(spelling_corrector ('your aret doins grat', ['you', 'live', 'the', 'doing', 'great', 'are']))

# thes is the first case
print(spelling_corrector('Thes is the Firs cas', ['that','first','case','car']))

# programming is fun and easy 
print(spelling_corrector('programing is fan and eesy', ['programming','this','fun','easy','book' ]))

# this is very easy 
print(spelling_corrector('Thes is vary essy', ['this', 'is', 'very', 'very', 'easy'] ))

# we live python
print(spelling_corrector('Wee lpve Pythen', ['we', 'Live', 'In', 'Python'] ))






