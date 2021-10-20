def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


n = 8
matrix = []

for _ in range(n):
    matrix.append(input().split())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_right': (-1, 1),
    'up_left': (-1, -1),
    'down_right': (1, 1),
    'down_left': (1, -1),
}

queens = []
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'Q':
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_in_range(next_row, next_col, n):
                    if matrix[next_row][next_col] == 'Q':
                        break
                    if matrix[next_row][next_col] == 'K':
                        queens.append([row, col])
                        break
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if queens:
    for queen in queens:
        print(queen)
else:
    print('The king is safe!')

