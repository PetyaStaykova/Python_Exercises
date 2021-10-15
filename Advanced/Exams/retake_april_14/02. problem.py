def is_valid_position(r, c, board, size):
    size = len(board)
    if r < 0 or r >= size or c < 0 or c >= size:
        return False
    return True


def hit_d(r, c, board, size):
    size = len(board)
    return (int(board[r][0]) + int(board[0][c]) + int(board[r][size - 1]) + int(board[size - 1][c])) * 2


def hit_t(r, c, board, size):
    size = len(board)
    return (int(board[r][0]) + int(board[0][c]) + int(board[r][size - 1]) + int(board[size - 1][c])) * 3


def check_if_wins(points, board, r, c):
    if points <= 0 or board[r][c] == 'B':
        return True
    return False


player_1, player_2 = input().split(', ')

n = 7
matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)
points_player_1 = 501
points_player_2 = 501
throws_player_1 = 0
throws_player_2 = 0
turn = 0
while True:
    command = input()[1:-1].split(',')
    row = int(command[0])
    col = int(command[1])
    turn += 1
    if turn % 2 == 1 and is_valid_position(row, col, matrix, n):
        current_player = player_1
        current_throw = throws_player_1
        current_points = points_player_1
        current_throw += 1
        if matrix[row][col] == 'D':
            current_points -= hit_d(row, col, matrix, n)
        elif matrix[row][col] == 'T':
            current_points -= hit_t(row, col, matrix, n)
        else:
            if not check_if_wins(current_points, matrix, row, col):
                number = matrix[row][col]
                current_points -= int(number)

        if check_if_wins(current_points, matrix, row, col):
            print(f'{current_player} won the game with {current_throw} throws!')
            break
        points_player_1 = current_points
        throws_player_1 = current_throw

    elif turn % 2 == 0 and is_valid_position(row, col, matrix, n):
        current_player = player_2
        current_throw = throws_player_2
        current_points = points_player_2
        current_throw += 1

        if matrix[row][col] == 'D':
            current_points -= hit_d(row, col, matrix, n)
        elif matrix[row][col] == 'T':
            current_points -= hit_t(row, col, matrix, n)
        else:
            if not check_if_wins(current_points, matrix, row, col):
                number = matrix[row][col]
                current_points -= int(number)

        if check_if_wins(current_points, matrix, row, col):
            print(f'{current_player} won the game with {current_throw} throws!')
            break

        points_player_2 = current_points
        throws_player_2 = current_throw
    else:
        if turn % 2 == 1:
            throws_player_1 += 1
        else:
            throws_player_2 += 1

