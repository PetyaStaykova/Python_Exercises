def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


word = input()
n = int(input())
matrix = []
player_position = None

for row in range(n):
    row_data = list(input())
    if 'P' in row_data:
        player_position = [row, row_data.index('P')]
    matrix.append(row_data)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

m_lines = int(input())
for line in range(m_lines):
    direction = input()
    if direction in directions:
        next_row = player_position[0] + directions[direction][0]
        next_col = player_position[1] + directions[direction][1]

        if is_in_range(next_row, next_col, n):
            if matrix[next_row][next_col] == '-':
                matrix[next_row][next_col] = 'P'
            else:
                word += matrix[next_row][next_col]
                matrix[next_row][next_col] = 'P'
            matrix[player_position[0]][player_position[1]] = '-'
            player_position = [next_row, next_col]

        else:
            word = word[:-1]
            matrix[player_position[0]][player_position[1]] = 'P'

print(word)
for row_el in matrix:
    print(''.join(row_el))
