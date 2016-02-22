def find_longest_word(some_string):
    words = some_string.split()
    longest_word = ''
    longest_word_length = 0

    for word in words:
        if len(word) >= longest_word_length:
            longest_word = word
            longest_word_length = len(word)
    
    return longest_word

print(find_longest_word('brahman the mysterious of the univERsity'))
