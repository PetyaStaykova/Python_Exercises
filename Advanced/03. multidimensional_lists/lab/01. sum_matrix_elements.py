n, m = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
sum_of_all_numbers = 0

for row_index in range(n):
    row = matrix[row_index]
    sum_of_all_numbers += sum(row)
print(sum_of_all_numbers)
print(matrix)