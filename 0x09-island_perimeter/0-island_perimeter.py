#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ The function description """
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                if grid[i][j] == 1:
                    if grid[i - 1][j] == 0:
                        p += 1
                    if grid[i][j - 1] == 0:
                        p += 1
                    if grid[i][j + 1] == 0:
                        p += 1
                    if grid[i + 1 ][j] == 0:
                        p += 1
            except Exception:
                pass
    return p
