# compare two strings
# return 0 if the two strings match exactly
# return 1 if the two strings have the same length and mismatch in only one character
# return 2 if the two strings do not have the same length or mismatch in two or more characters
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
        
##print(find_mismatch('Python','Java'))
##print(find_mismatch('Hello There','helloothere'))
##print(find_mismatch('sin','sink'))
##print(find_mismatch('dog','Dog'))
