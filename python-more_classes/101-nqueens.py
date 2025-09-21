#!/usr/bin/python3
"""N Queens problem solver"""

import sys


def main():
    """Main function"""
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

    def is_safe(board, row, col):
        """Check if position is safe for queen"""
        # Check row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal
        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve(board, col, solutions):
        """Backtracking solution"""
        if col == N:
            # Convert to required format
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 1
                solve(board, col + 1, solutions)
                board[i][col] = 0  # backtrack

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
