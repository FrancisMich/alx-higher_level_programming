#!/usr/bin/python3

"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
"""
import sys


def create_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def copy_board(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def mark_positions(board, row, col):
    """Mark all positions where non-attacking queens can no
    longer be placed with an 'x'
    """
    # Mark all forward positions
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Mark all backward positions
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Mark all positions below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Mark all positions above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Mark all positions diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    # Mark all positions diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Mark all positions diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
      c -=
