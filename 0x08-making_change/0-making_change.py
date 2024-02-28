#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
        determine the fewest number of coins needed
        to meet a given amount total.
    """
    if total <= 0:
        return (0)

    coins = sorted(coins)
    count = 0
    length = len(coins)
    i = (length - 1)
    while i >= 0:
        if not total:
            break
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i -= 1
    if total:
        return (-1)
    return (count)
