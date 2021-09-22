a_from_table = ord('a')

for first_letter in range(a_from_table, a_from_table + n):
    for second_letter in range(a_from_table, a_from_table + n):
        for third_letter in range(a_from_table, a_from_table + n):
            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}')