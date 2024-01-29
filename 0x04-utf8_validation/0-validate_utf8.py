#!/usr/bin/python3
""" Write a method that determines if a given data set
    represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Method that determines if a given data
        set represents a valid UTF-8 encoding
    """
    data_has_len = False

    if not isinstance(data, list): return (False)

    for item in data:
        data_has_len = True
        if item < 0 or item > 255: return (False)


    return (data_has_len)
