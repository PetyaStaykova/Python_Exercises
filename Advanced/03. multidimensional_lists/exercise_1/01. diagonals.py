n = int(input())
matrix = []
primary = []
secondary = []

for row in range(n):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(n):
    primary.append(matrix[row][row])
    secondary.append(matrix[row][n - 1 - row])

print(f'Primary diagonal: {", ".join([str(x) for x in primary])}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary])}. Sum: {sum(secondary)}')