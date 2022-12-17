START_STONES = 7
FINAL_STONES = 61
MAX_STONES = FINAL_STONES * 2 - 1

game = [
    [
        0 if i+j >= FINAL_STONES else -1
        for j in range(MAX_STONES)
    ]
    for i in range(MAX_STONES)
]


def can_win(moves):
    for move in moves:
        if move % 2 == 0:
            return True
    return False


def loses(moves):
    for move in moves:
        if move % 2 == 0 or move < 0:
            return False
    return True


def check_pos(i, j, moves_left):
    if game[i][j] == -1:
        moves = [
            game[i+1][j],
            game[i*2][j],
            game[i][j+1],
            game[i][j*2],
        ]
        if moves_left % 2 == 1:
            if can_win(moves):
                game[i][j] = moves_left
        else:
            if loses(moves):
                game[i][j] = moves_left


def solve_game():
    for moves_left in range(1, 5):
        for i in range(START_STONES, FINAL_STONES):
            for j in range(1, FINAL_STONES):
                check_pos(i, j, moves_left)


if __name__ == '__main__':
    solve_game()
    for j in range(1, FINAL_STONES):
        if game[START_STONES][j] == 4:
            print(j, game[START_STONES][j])

    print("Done")
