'''
A function named find_word_vertical that accepts a 2-dimensional list of characters
(like a crossword puzzle) and a string (word) as input arguments.
'''
def find_word_vertical(crosswords,word):
    found_word = False
    number_of_rows = len(crosswords)
    number_of_colums = len(crosswords[0])
    for col_index in range(0, number_of_colums):
        # get vertical word
        vertical_word = ''
        for ri in range(0, number_of_rows):
            vertical_word = vertical_word + crosswords[ri][col_index]

        row_index = vertical_word.find(word)
        if row_index >= 0:
            found_word = True
            return [row_index, col_index]
            break

    return None

# Sample test below
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
print(find_word_vertical(crosswords, word))
