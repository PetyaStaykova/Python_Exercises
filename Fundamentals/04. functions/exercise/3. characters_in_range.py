def chars_in_range(start_char, end_char):
    start_int = ord(start_char)
    end_int = ord(end_char)
    characters = []

    for n in range(start_int +1 , end_int):
        characters.append(chr(n))
    return characters


first_char = input()
second_char = input()
result = chars_in_range(first_char, second_char)
print(' '.join(result))

