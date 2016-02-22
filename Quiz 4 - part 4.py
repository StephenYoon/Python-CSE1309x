# Two strings are anagrams if one string can be constructed by rearranging the
# characters in the other string using all the characters in the original string
# exactly once
def test_for_anagrams(my_string1, my_string2):
    letters1 = sorted(list(my_string1.lower()))
    letters2 = sorted(list(my_string2.lower()))
    return letters1 == letters2

print(test_for_anagrams('Orchestra', 'Carthorse'))
