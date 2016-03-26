'''
A function named find_word_horizontal that accepts a 2-dimensional list of characters
(like a crossword puzzle) and a string (word) as input arguments.
This function searches the rows of the 2d list to find a match for the word.
If a match is found, this functions returns a list
containing row index and column index of the start of the match,
otherwise it returns the value None (no quotations). 
'''
def find_word_horizontal(crosswords,word):
    row_index = 0
    col_index = 0
    found_word = False
    for row_index in range(0, len(crosswords)):
        row_word = ''.join(crosswords[row_index])
        col_index = row_word.find(word)
        if col_index >= 0:
            found_word = True
            return [row_index, col_index]
            break

    return None

# Sample test below
crosswords=[['s','d','o','g'],['c','u','c','m'],['b','c','a','t'],['t','e','t','k']]
word='bat'
print(find_word_horizontal(crosswords, word))
