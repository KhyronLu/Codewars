"""
Name : Tic-Tac-Toe Checker.py
Author  : KhyronLu
Time    : 2021/7/4 11:24 下午
Desc:
"""


def isSolved(board):
    # We'll begin by checking for a horizontal win:

    for i in range(0, 3):
        if len(set(board[i])) == 1:
            if board[i][0] == 1:
                return 1
            if board[i][0] == 2:
                return 2

        # Next we'll check for a vertical win:

        if len(set([board[0][i], board[1][i], board[2][i]])) == 1:
            if board[0][i] == 1:
                return 1
            if board[0][i] == 2:
                return 2

    # Then we'll check for a diagonal win:

    if (len(set([board[0][0], board[1][1], board[2][2]])) == 1) | (
            len(set([board[0][2], board[1][1], board[2][0]])) == 1):
        if board[1][1] == 1:
            return 1
        if board[1][1] == 2:
            return 2

    # If we've made it to this line, there are two possibilities
    # remaining. So we'll look for a blank space:

    for i in range(0, 3):
        if 0 in board[i]:
            return -1

    # If we've made it to this line, there is only one possibility
    # remaining: a cat's game.

    return 0