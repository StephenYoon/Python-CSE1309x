def my_encryption(some_string):
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    characters = list(character_set)
    secrets = list(secret_key)
    letters = list(some_string)

    secret_code = []
    for letter in letters:
        letter_index = characters.index(letter)
        secret_letter = secrets[letter_index]
        secret_code.append(secret_letter)

    return ''.join(secret_code)

print(my_encryption('Lets meet at the usual place at 9 am'))
