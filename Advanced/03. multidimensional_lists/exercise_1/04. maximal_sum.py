rows, columns = [int(x) for x in input().split()]
matrix = []
max_sum = 0
best_row = 0
best_column = 0

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for r in range(rows - 2):
    for c in range(columns - 2):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r][c + 2] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1] +\
                      matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + \
                      matrix[r + 2][c + 1] + \
                      matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum, best_row, best_column = current_sum, r, c
print(f'Sum = {max_sum}')
print(matrix[best_row][best_column], matrix[best_row][best_column + 1], matrix[best_row][best_column + 2])
print(matrix[best_row + 1][best_column], matrix[best_row + 1][best_column + 1], matrix[best_row + 1][best_column + 2])
print(matrix[best_row + 2][best_column], matrix[best_row + 2][best_column + 1], matrix[best_row + 2][best_column + 2])
