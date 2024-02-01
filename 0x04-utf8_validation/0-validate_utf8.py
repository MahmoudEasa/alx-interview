#!/usr/bin/python3
""" Write a method that determines if a given data set
    represents a valid UTF-8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Method that determines if a given data
        set represents a valid UTF-8 encoding
    """
    n_bytes = 0

    for item in data:
        item %= 256
        if n_bytes == 0:
            if (item >> 7) == 0b0:
                continue

            if (item >> 5) == 0b110:
                n_bytes = 1
            elif (item >> 4) == 0b1110:
                n_bytes = 2
            elif (item >> 3) == 0b11110:
                n_bytes = 3
            else:
                return (False)
        else:
            if (item >> 6) != 0b10:
                return (False)
            n_bytes -= 1

    return (n_bytes == 0)
