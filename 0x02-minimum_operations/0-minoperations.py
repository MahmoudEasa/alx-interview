#!/usr/bin/python3
""" In a text file, there is a single character H.
    Your text editor can execute only two operations
    in this file: Copy All and Paste. Given a number n,
    write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """ Min Operations Function """
    if type(n) != int or n < 2:
        return (0)

    min = 2
    opr = 2

    if n % 2 != 0:
        opr += 1
        min += 1

    copy_all = opr

    while (opr < n):
        if (opr + opr <= n):
            opr += opr
            copy_all = opr
            min += 2

        else:
            opr += copy_all
            min += 1

    return (min)
