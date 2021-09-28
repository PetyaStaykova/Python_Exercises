rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])


for c in range(columns):
    sum_column = 0
    for r in range(rows):
        sum_column += matrix[r][c]
    print(sum_column)