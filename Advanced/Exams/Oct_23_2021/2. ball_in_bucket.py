def is_in_range(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def sum_columns(r, c, size, board):
    sum_column = 0
    for r in range(size):
        if board[r][c].isnumeric():
            sum_column += int(board[r][c])
    return sum_column


def prize_won(score):
    if score < 100:
        return f'Sorry! You need {100 - score} points more to win a prize.'
    elif 100 <= score <= 199:
        return f'Good job! You scored {score} points, and you\'ve won Football.'
    elif 200 <= score <= 299:
        return f'Good job! You scored {score} points, and you\'ve won Teddy Bear.'
    else:
        return f'Good job! You scored {score} points, and you\'ve won Lego Construction Set.'


n = 6
matrix = []
points = 0
for _ in range(n):
    matrix.append(input().split())
b_positions = []
for i in range(3):
    hit_info = input()[1:-1].split(',')
    row = int(hit_info[0])
    col = int(hit_info[1])
    if is_in_range(row, col, n):
        if matrix[row][col] == 'B':
            if (row, col) not in b_positions:
                points += sum_columns(row, col, n, matrix)
                b_positions.append((row, col))

print(prize_won(points))