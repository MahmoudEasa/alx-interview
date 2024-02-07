#!/usr/bin/python3
import sys

"""Module to solves the N queens problem
"""


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

num_s = sys.argv[1]

if not num_s.isdigit():
    print("N must be a number")
    exit(1)

n = int(num_s)

if n < 4:
    print("N must be at least 4")
    exit(1)

arr = [[0 for i in range(n)] for j in range(n)]


def is_col_safe(arr, col, n):
    for i in range(n):
        if arr[i][col] == 1:
            return (1)
    return (0)


def is_row_safe(arr, row, n):
    for i in range(n):
        if arr[row][i] == 1:
            return (1)
    return (0)


def is_dbr_safe(arr, row, col, n):
    while (row < n and col < n):
        if arr[row][col] == 1:
            return (1)
        row += 1
        col += 1
    return (0)


def is_dbl_safe(arr, row, col, n):
    while (row < n and col >= 0):
        if arr[row][col] == 1:
            return (1)
        row += 1
        col -= 1
    return (0)


def is_dtr_safe(arr, row, col, n):
    while (row >= 0 and col >= 0):
        if arr[row][col] == 1:
            return (1)
        row -= 1
        col -= 1
    return (0)


def is_dtl_safe(arr, row, col, n):
    while (row >= 0 and col < n):
        if arr[row][col] == 1:
            return (1)
        row -= 1
        col += 1
    return (0)


def solution(arr, n):
    c = 0
    r = 0
    n_len = 0
    track = 0
    index = []
    result = []

    while (c >= 0 and c < n):
        if is_col_safe(arr, c, n):
            if track:
                arr[c][index[-1]] = 0
                r = index[-1]
                index.pop()
                result.pop()
            else:
                c += 1
                continue
        while (r >= 0 and r < n):
            if is_row_safe(arr, r, n):
                r += 1
                continue
            if is_dbr_safe(arr, r, c, n):
                r += 1
                continue
            if is_dbl_safe(arr, r, c, n):
                r += 1
                continue
            if is_dtr_safe(arr, r, c, n):
                r += 1
                continue
            if is_dtl_safe(arr, r, c, n):
                r += 1
                continue

            arr[r][c] = 1
            result.append([c, r])
            index.append(r)
            r = 0
            break
        if r == n:
            c -= 1
            if len(index) > 0:
                arr[index[-1]][c] = 0
                r = index[-1] + 1
                index.pop()
                result.pop()
            continue
        c += 1
        if c == n and len(index) > 0:
            print(result)
            result = []
            r = index[0] + 1
            c = 0
            index = []
            track = 0
            arr = [[0 for i in range(n)] for j in range(n)]


solution(arr, n)


'''
#!/usr/bin/python3
""" A program that solves the N queens problem
"""
from sys import argv


def check_row(board, index, board_len):
    """ Check if there is a queen in the row """
    for r in range(board_len):
        if board[index][r]:
            return (False)

    return (True)


def check_r_angle(board, row, col, board_len):
    """ Check if there is a queen in the left angle """
    c = col
    for r in range(row, -1, -1):
        if c >= board_len:
            break
        if board[r][c]:
            return (False)
        c += 1

    c = col
    for r in range(row, board_len):
        if c < 0:
            break
        if board[r][c]:
            return (False)
        c -= 1

    return (True)


def check_l_angle(board, row, col, board_len):
    """ Check if there is a queen in the right angle """
    c = col
    for r in range(row, -1, -1):
        if c < 0:
            break
        if board[r][c]:
            return (False)
        c -= 1

    c = col
    for r in range(row, board_len):
        if c >= board_len:
            break
        if board[r][c]:
            return (False)
        c += 1

    return (True)


def chek_all(board, r, c, n):
    if not check_row(board, r, n):
        return (False)

    if not check_l_angle(board, r, c, n):
        return (False)

    return (check_r_angle(board, r, c, n))


def main():
    """ The Main Function """

    argc = len(argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    n_range = range(n)
    i = 0
    while i < n:
        board = [[0 for _ in n_range] for _ in n_range]
        result = []
        c = 0
        r = i

        while (c < n):
            found = 0

            while (r < n):
                if r >= n:
                    break

                if chek_all(board, r, c, n):
                    board[r][c] = 1
                    result.append([c, r])
                    found = 1
                    r = 0
                    break
                r += 1

            if not found and len(result):
                last_i = result.pop()
                c = last_i[0]
                r = last_i[1] + 1
                board[last_i[1]][last_i[0]] = 0
                continue
            c += 1

        if len(result):
            print(result)
            i = result[0][1] + 1
        else:
            return


if __name__ == "__main__":
    main()
'''
