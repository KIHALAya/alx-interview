#!/usr/bin/python3
""" N queens
"""

import sys


def print_solution(board, N):
    """Print a board configuration as a list of queen positions."""
    solution = [[i, j] for i in range(N) for j in range(N) if board[i][j] == 1]
    print(solution)


def is_safe(board, row, col, N):
    """Check if a queen can be safely placed at (row, col)."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, N):
    """Use backtracking to place queens in all columns."""
    if col >= N:
        print_solution(board, N)
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N)
            board[i][col] = 0  # Backtrack


def solve_nqueens(N):
    """Initialize the board and solve the N Queens problem."""
    board = [[0] * N for _ in range(N)]
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
