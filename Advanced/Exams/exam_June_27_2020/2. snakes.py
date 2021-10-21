def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def find_burrow(r, c, matrix, size):
    burrow_exit_position = None
    burrow_count = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                burrow_count += 1
                if burrow_count == 2:
                    burrow_exit_position = [r, c]
                    break
    return burrow_exit_position


n = int(input())
matrix = []
snake_position = None

for row in range(n):
    row_data = list(input())
    if 'S' in row_data:
        snake_position = [row, row_data.index('S')]
    matrix.append(row_data)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
food_eaten = 0

while True:
    direction = input()
    if direction in directions:
        next_row = snake_position[0] + directions[direction][0]
        next_col = snake_position[1] + directions[direction][1]
        if is_in_range(next_row, next_col, n):
            if matrix[next_row][next_col] == '-':
                matrix[next_row][next_col] = 'S'
                matrix[snake_position[0]][snake_position[1]] = '.'
                snake_position = [next_row, next_col]
            elif matrix[next_row][next_col] == 'B':
                matrix[snake_position[0]][snake_position[1]] = '.'
                snake_position = find_burrow(next_row, next_col, matrix, n)
                matrix[snake_position[0]][snake_position[1]] = 'S'
                matrix[next_row][next_col] = '.'
            elif matrix[next_row][next_col] == '*':
                matrix[snake_position[0]][snake_position[1]] = '.'
                food_eaten += 1
                snake_position = [next_row, next_col]
                matrix[next_row][next_col] = 'S'
                if food_eaten >= 10:
                    print('You won! You fed the snake.')
                    break
        else:
            matrix[snake_position[0]][snake_position[1]] = '.'
            print('Game over!')
            break
print(f'Food eaten: {food_eaten}')
for row in matrix:
    print(''.join(row))