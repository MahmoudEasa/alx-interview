#!/usr/bin/python3

def SieveOfEratosthenes(n):
    """ Implementing the sieve algorithm in Python """
    prime = [True for i in range(n+1)]
    p = 2
    result = []
    while (p * p <= n):
        if (prime[p] is True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            result.append(p)
    return (result)


def isWinner(x, nums):
    """ Prime Game
        where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        If the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
    """

    b_win, m_win = 0, 0

    if not x or x > len(nums):
        return (None)

    for i in range(x):
        primes = len(SieveOfEratosthenes(nums[i]))
        if primes % 2 == 0:
            b_win += 1
        else:
            m_win += 1

    if b_win > m_win:
        return "Ben"
    else:
        return "Maria"
