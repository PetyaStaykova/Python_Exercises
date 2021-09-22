n_lines = int(input())
total_sum = 0

for i in range(n_lines):
    letter = input()
    num_from_letter = ord(letter)
    total_sum += num_from_letter

print(f'The sum equals: {total_sum}')