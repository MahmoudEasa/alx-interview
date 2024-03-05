#!/usr/bin/python3
""" The Island Perimeter
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    perimeter = 0
    row_len = len(grid)
    col_len = len(grid[0])

    for row in range(1, row_len - 1):
        for col in range(1, col_len - 1):
            if grid[row][col]:
                if not grid[row - 1][col]:
                    perimeter += 1
                if not grid[row + 1][col]:
                    perimeter += 1
                if not grid[row][col - 1]:
                    perimeter += 1
                if not grid[row][col + 1]:
                    perimeter += 1
    return (perimeter)
