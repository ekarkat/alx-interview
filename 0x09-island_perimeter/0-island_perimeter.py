#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ The function description """
    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                if grid[i][j] == 1:
                    if not grid[i - 1][j]:
                        p += 1
                    if not grid[i][j - 1]:
                        p += 1
                    if not grid[i][j + 1]:
                        p += 1
                    if not grid[i + 1 ][j]:
                        p += 1
            except Exception:
                pass
    return p
