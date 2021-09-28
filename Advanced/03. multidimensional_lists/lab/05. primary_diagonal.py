n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

sum_diagonal = []
for r in range(n):
    sum_diagonal.append(matrix[r][r])
print(sum(sum_diagonal))