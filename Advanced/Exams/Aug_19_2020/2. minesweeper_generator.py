def fill_matrix(matrix: list, r: int, c: int):
    matrix[r][c] = '*'
    if not r == 0:
        if not matrix[r-1][c] == '*':
            matrix[r - 1][c] += 1
    if not r == len(matrix) - 1:
        if not matrix[r+1][c] == '*':
            matrix[r + 1][c] += 1
    if not c == 0:
        if not matrix[r][c-1] == '*':
            matrix[r][c - 1] += 1
    if not c == len(matrix) - 1:
        if not matrix[r][c+1] == '*':
            matrix[r][c + 1] += 1
    if not r == 0 and not c == 0:
        if not matrix[r-1][c-1] == '*':
            matrix[r - 1][c - 1] += 1
    if not r == len(matrix) - 1 and not c == len(matrix) - 1:
        if not matrix[r+1][c+1] == '*':
            matrix[r + 1][c + 1] += 1
    if not r == 0 and not c == len(matrix) - 1:
        if not matrix[r-1][c+1] == '*':
            matrix[r - 1][c + 1] += 1
    if not r == len(matrix) - 1 and not c == 0:
        if not matrix[r+1][c-1] == '*':
            matrix[r + 1][c - 1] += 1


n = int(input())
n_positions = int(input())
matrix = []
for _ in range(n):
    matrix.append([0]*n)

for p in range(n_positions):
    position = input()[1:-1].split(', ')
    row = int(position[0])
    col = int(position[1])
    fill_matrix(matrix, row, col)

for row in matrix:
    print(' '.join([str(x) for x in row]))
