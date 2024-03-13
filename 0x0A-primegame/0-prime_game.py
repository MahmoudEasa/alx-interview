#!/usr/bin/python3
""" Prime Game """


def SieveOfEratosthenes(n):
    """ Implementing the sieve algorithm in Python """
    prime = [True for i in range(n+1)]
    p = 2
    result = 0
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            result += 1
    return (result)


def isWinner(x, nums):
    """ Solve Prime Game """

    b_win, m_win = 0, 0

    if not x:
        return (None)

    for i in range(x):
        primes = SieveOfEratosthenes(nums[i])
        if primes % 2 == 0:
            b_win += 1
        else:
            m_win += 1

    if b_win > m_win:
        return ("Ben")
    elif m_win > b_win:
        return ("Maria")
    else:
        return (None)
