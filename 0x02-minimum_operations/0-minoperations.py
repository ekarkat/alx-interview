#!/usr/bin/python3
"""Documentation"""


def minOperations(n):
    """ALX interview"""
    num = 2
    step = 0
    op = 2
    change = False
    if n == 0 or n == 1:
        return 0

    for j in range(n):
        if num == n:
            return op
        if n % num == 0:
            step = num
            num = num + num
            op = op + 2
            change = True
        else:
            if change:
                num = num + step
            else:
                num = num + 1
            op = op + 1
