def count_consonants(some_string):
    mylist = list(some_string)
    consonants = list("bcdfghjklmnpqrstvwxyz")
    consonant_count = 0;
    for letter in mylist:
        if letter.lower() in consonants:
            consonant_count = consonant_count + 1

    return consonant_count

print(count_consonants('Hercules was a hero'))
