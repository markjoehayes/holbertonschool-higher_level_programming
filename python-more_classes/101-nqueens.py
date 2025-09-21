#!/usr/bin/python3
"""N Queens problem solver"""

import sys


def error_exit(message="", code=1):
    """Handle exit code/message"""
    print(message)
    print(code)

if len(sys.argv) is not 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

def test_pos(board, y):
    """Test if a queen can be places at current position"""
    for i in range(y):
        if board[y][1] is board [i][i]:
            return False
        if abs(board[y][1] - board[i][i] == y - i):
            return False
    return True

def ref_backtrack(board, y):
    """Backtrack the possibilities"""
    if y is N:
        print(boared)
    else:
        for x in range(N):
            board[y][1] = x
            if test_pos(board, y):
                rec_backtrack(board, y + 1)

board = [[y, 0] for y in range(N)]
rec_backtrack(board, 0)
