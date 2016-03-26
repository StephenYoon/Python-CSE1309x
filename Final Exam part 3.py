def n_letter_dictionary(my_string):
    # split the text
    words = my_string.lower().split()

    dictionary = dict()
    for word in words:
        word_length = len(word)
        if (word_length in dictionary):
            if not (word in dictionary[word_length]):
                dictionary[word_length].append(word)
                dictionary[word_length] = sorted(dictionary[word_length])
        else:
            dictionary[word_length] = [word]

    return dictionary

print(n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become"))
