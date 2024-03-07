#!/usr/bin/python3
""" Pascal triangle module"""


def pascal_triangle(n):
    """ Pascal Triangle """
    if n == 0:
        return []
    pascal_list = []
    for i in range(n):
        row = []
        len_p = len(pascal_list)
        for j in range(i + 1):
            if j == 0:
                row.append(1)
            if (j == len_p and j != 0):
                row.append(1)
                break
            if (j < len_p and j != 0):
                last_row = pascal_list[len_p - 1]
                row.append(last_row[j-1] + last_row[j])

        pascal_list.append(row)

    return pascal_list
