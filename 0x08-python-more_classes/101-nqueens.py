#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking.
"""


def is_safe(m_queen, nqueen):
    """
    Determine if the queens can or can't kill each other.

    Args:
        m_queen: List that has the queens' positions.
        nqueen: Index of the queen to check.

    Returns:
        bool: True if queens can't kill each other, False otherwise.
    """
    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen]:
            return False
        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False
    return True


def print_result(m_queen, nqueen):
    """
    Print the list with the queens' positions.

    Args:
        m_queen: List that has the queens' positions.
        nqueen: Current number of queens placed.
    """
    result = [[i, m_queen[i]] for i in range(nqueen)]
    print(result)


def queen(m_queen, nqueen):
    """
    Recursive function that executes the backtracking algorithm.

    Args:
        m_queen: List that has the queens' positions.
        nqueen: Current index to place the queen.
    """
    if nqueen == len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while m_queen[nqueen] < len(m_queen) - 1:
        m_queen[nqueen] += 1

        if is_safe(m_queen, nqueen):
            if nqueen + 1 < len(m_queen):
                queen(m_queen, nqueen + 1)


def solve_n_queen(size):
    """
    Invoke the backtracking algorithm to solve the N-Queen problem.

    Args:
        size: Size of the chessboard.
    """

    m_queen = [-1] * size
    queen(m_queen, 0)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queen(size)
