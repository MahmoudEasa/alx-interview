#!/usr/bin/python3
""" The Island Perimeter
"""


def check_index(grid, row_len, col_len, row, col):
    """ Check index and if grid[row][col] = 0 """
    if row >= row_len or col >= col_len or \
            row < 0 or col < 0 or grid[row][col] == 0:
        return (1)
    else:
        return (0)


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    perimeter = 0

    if isinstance(grid, list):
        row_len = len(grid)
        col_len = len(grid[0])
        if all(isinstance(grid[i], list) for i in range(row_len)):
            for row in range(row_len):
                for col in range(col_len):
                    if grid[row][col]:
                        perimeter += check_index(grid, row_len,
                                                 col_len, row - 1, col)
                        perimeter += check_index(grid, row_len,
                                                 col_len, row + 1, col)
                        perimeter += check_index(grid, row_len,
                                                 col_len, row, col - 1)
                        perimeter += check_index(grid, row_len,
                                                 col_len, row, col + 1)
    return (perimeter)
