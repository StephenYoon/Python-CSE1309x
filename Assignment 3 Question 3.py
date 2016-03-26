def find_word_horizontal(crosswords,word):
    row_index = 0
    col_index = 0
    for row_index in range(0, len(crosswords)):
        row_word = ''.join(crosswords[row_index])
        col_index = row_word.find(word)
        if col_index >= 0:
            for i in range(0, len(word)):
                crosswords[row_index][col_index + i] = crosswords[row_index][col_index + i].upper()
            return [row_index, col_index]
            break

    return None

def find_word_vertical(crosswords,word):
    number_of_rows = len(crosswords)
    number_of_colums = len(crosswords[0])
    for col_index in range(0, number_of_colums):
        # get vertical word
        vertical_word = ''
        for ri in range(0, number_of_rows):
            vertical_word = vertical_word + crosswords[ri][col_index]

        row_index = vertical_word.find(word)
        if row_index >= 0:
            for i in range(0, len(word)):
                crosswords[row_index + i][col_index] = crosswords[row_index + i][col_index].upper()
            return [row_index, col_index]
            break

    return None

def capitalize_word_in_crossword (crosswords,word):
    found_word = find_word_horizontal(crosswords,word)
    if (found_word != None):
        return crosswords
    
    found_word = find_word_vertical(crosswords,word)
    if (found_word != None):
        return crosswords

    return crosswords


# Sample test below
#crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
#word='cat'
print(capitalize_word_in_crossword([['a', 'b'], ['c', 'd']], 'ac'))


