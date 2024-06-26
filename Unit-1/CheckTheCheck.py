def handle_straight(board, x, y, target1, target2):
    if (x - 1 >= 0 and (board[y][x - 1] == target1 or board[y][x - 1] == target2)) or \
       (x + 1 < 8 and (board[y][x + 1] == target1 or board[y][x + 1] == target2)) or \
       (y - 1 >= 0 and (board[y - 1][x] == target1 or board[y - 1][x] == target2)) or \
       (y + 1 < 8 and (board[y + 1][x] == target1 or board[y + 1][x] == target2)):
        return True

    for xc in range(-1, -x - 1, -1):
        if board[y][xc + x] != '.':
            if board[y][xc + x] == target1 or board[y][xc + x] == target2:
                return True
            break

    for xc in range(1, 8 - x):
        if board[y][xc + x] != '.':
            if board[y][xc + x] == target1 or board[y][xc + x] == target2:
                return True
            break

    for yc in range(-1, -y - 1, -1):
        if board[yc + y][x] != '.':
            if board[yc + y][x] == target1 or board[yc + y][x] == target2:
                return True
            break

    for yc in range(1, 8 - y):
        if board[yc + y][x] != '.':
            if board[yc + y][x] == target1 or board[yc + y][x] == target2:
                return True
            break

    return False


def handle_diagonal(board, x, y, target1, target2):
    up_left = up_right = down_left = down_right = True

    for c in range(1, 8):
        if up_left:
            if x - c >= 0 and y - c >= 0:
                if board[y - c][x - c] == target1 or board[y - c][x - c] == target2:
                    return True
                elif board[y - c][x - c] != '.':
                    up_left = False
            else:
                up_left = False

        if up_right:
            if x + c < 8 and y - c >= 0:
                if board[y - c][x + c] == target1 or board[y - c][x + c] == target2:
                    return True
                elif board[y - c][x + c] != '.':
                    up_right = False
            else:
                up_right = False

        if down_left:
            if x - c >= 0 and y + c < 8:
                if board[y + c][x - c] == target1 or board[y + c][x - c] == target2:
                    return True
                elif board[y + c][x - c] != '.':
                    down_left = False
            else:
                down_left = False

        if down_right:
            if x + c < 8 and y + c < 8:
                if board[y + c][x + c] == target1 or board[y + c][x + c] == target2:
                    return True
                elif board[y + c][x + c] != '.':
                    down_right = False
            else:
                down_right = False

    return False


def handle_knight(board, x, y, target):
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
    for move in knight_moves:
        new_x, new_y = x + move[0], y + move[1]
        if 0 <= new_x < 8 and 0 <= new_y < 8 and board[new_y][new_x] == target:
            return True
    return False


def handle_pawn(board, x, y, target, y_change):
    if 0 <= y + y_change < 8:
        if x - 1 >= 0 and board[y + y_change][x - 1] == target:
            return True
        if x + 1 < 8 and board[y + y_change][x + 1] == target:
            return True
    return False


def main():
    forever = True
    t = 1

    while forever:
        board = [input().strip() for _ in range(8)]
        input()  # consume the blank line

        white_posx = black_posx = -1

        for i in range(8):
            temp = board[i].find('k')
            if temp != -1:
                black_posy = i
                black_posx = temp
            temp = board[i].find('K')
            if temp != -1:
                white_posy = i
                white_posx = temp

        if white_posx == -1:
            break

        print(f"Game #{t}: ", end="")
        t += 1

        if handle_pawn(board, white_posx, white_posy, 'p', -1):
            print("white king is in check.")
        elif handle_pawn(board, black_posx, black_posy, 'P', 1):
            print("black king is in check.")
        elif handle_knight(board, white_posx, white_posy, 'n'):
            print("white king is in check.")
        elif handle_knight(board, black_posx, black_posy, 'N'):
            print("black king is in check.")
        elif handle_straight(board, white_posx, white_posy, 'r', 'q'):
            print("white king is in check.")
        elif handle_straight(board, black_posx, black_posy, 'R', 'Q'):
            print("black king is in check.")
        elif handle_diagonal(board, white_posx, white_posy, 'b', 'q'):
            print("white king is in check.")
        elif handle_diagonal(board, black_posx, black_posy, 'B', 'Q'):
            print("black king is in check.")
        else:
            print("no king is in check.")


if __name__ == "__main__":
    main()
