#!/usr/bin/python3
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for m in range(n)]
    [row.append(' ') for m in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for s in range(len(board)):
        for t in range(len(board)):
            if board[s][t] == "Q":
                solution.append([s, t])
                break
    return (solution)


def xout(board, row, col):
    # X out all forward spots
    for t in range(col + 1, len(board)):
        board[row][t] = "x"
    # X out all backwards spots
    for t in range(col - 1, -1, -1):
        board[row][t] = "x"
    # X out all spots below
    for s in range(row + 1, len(board)):
        board[s][col] = "x"
    # X out all spots above
    for s in range(row - 1, -1, -1):
        board[s][col] = "x"
    # X out all spots diagonally down to the right
    t = col + 1
    for s in range(row + 1, len(board)):
        if t >= len(board):
            break
        board[s][t] = "x"
        t += 1
    # X out all spots diagonally up to the left
    t = col - 1
    for s in range(row - 1, -1, -1):
        if t < 0:
            break
        board[s][t]
        t -= 1
    # X out all spots diagonally up to the right
    t = col + 1
    for s in range(row - 1, -1, -1):
        if t >= len(board):
            break
        board[s][t] = "x"
        s += 1
    # X out all spots diagonally down to the left
    t = col - 1
    for s in range(row + 1, len(board)):
        if t < 0:
            break
        board[s][t] = "x"
        t -= 1


def recursive_solve(board, row, queens, solutions):
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for t in range(len(board)):
        if board[row][t] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][t] = "Q"
            xout(tmp_board, row, t)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
