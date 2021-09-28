n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input())

symbol = input()
is_symbol_found = False
row, col = None, None

for r in range(len(matrix)):
    if is_symbol_found:
        break
    for c in range(len(matrix)):
        if matrix[r][c] == symbol:
            row, col = r, c
            is_symbol_found = True
            break

if is_symbol_found:
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')