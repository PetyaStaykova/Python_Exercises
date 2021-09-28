def valid_position(r, c, rows, cols):
    if 0 < r >= rows or 0 < c >= cols:
        return False
    return True


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break
    command_info = command.split()
    if command_info[0] != 'swap' or len(command_info) != 5:
        print('Invalid input!')
        continue
    row_1, col_1, row_2, col_2 = [int(x) for x in command_info[1:]]
    if not valid_position(row_1, col_1, rows, cols) or not valid_position(row_2, col_2, rows, cols):
        print('Invalid input!')
        continue
    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

    for el in matrix:
        print(' '.join([str(x) for x in el]))