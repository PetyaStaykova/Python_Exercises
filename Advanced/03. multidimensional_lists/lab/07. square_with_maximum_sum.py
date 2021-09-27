rows, cols = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
sums = []
n = len(matrix)
m = len(matrix[0])
max_sum = 0
position = None
for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            position = (r, c)
r, c = position
print(matrix[r][c], matrix[r][c+1])
print(matrix[r+1][c], matrix[r+1][c+1])
print(max_sum)
