#!/usr/bin/python3
""" Rotate 2D Matrix
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """ Rotate 2D Matrix """
    matrix_len = len(matrix)
    m_len = (matrix_len - 1)
    i = m_len
    c = 0
    start = 0
    while m_len:
        while c < m_len:
            tmp = matrix[start][i]
            matrix[start][i] = matrix[c][start]
            matrix[c][start] = matrix[m_len][c]
            matrix[m_len][c] = matrix[i][m_len]
            matrix[i][m_len] = tmp
            c += 1
            i -= 1
        m_len -= 1
        start += 1
        c = start
        i = m_len
