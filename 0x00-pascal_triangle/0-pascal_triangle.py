#!/usr/bin/python3
"""Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """ Pascal Triangle function """
    result = []

    if n > 0:
        for i in range(n):
            res_len = len(result)

            if res_len:
                res_len = len(result[-1])

            row = []

            for j in range(res_len + 1):
                if res_len < 2:
                    row.append(1)
                else:
                    if not j or j == res_len:
                        row.append(1)
                    else:
                        row.append(result[-1][j] + result[-1][j - 1])

            result.append(row)

    return (result)
