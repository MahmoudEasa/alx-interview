#!/usr/bin/python3
""" The Island Perimeter
"""


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
                        if row > 0 and not grid[row - 1][col]:
                            perimeter += 1
                        if row < (row_len - 1) and not grid[row + 1][col]:
                            perimeter += 1
                        if col > 0 and not grid[row][col - 1]:
                            perimeter += 1
                        if col < (col_len - 1) and not grid[row][col + 1]:
                            perimeter += 1
    return (perimeter)
