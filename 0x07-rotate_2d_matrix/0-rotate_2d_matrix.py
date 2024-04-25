#!/usr/bin/python3
""" 2DMatrix Rotate"""


def rotate_2d_matrix(matrix):
    """ Matrix Rotater """
    n = len(matrix)
    cmat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            cmat[i][j] = matrix[n - j - 1][i]
    i = 0
    for row in cmat:
        matrix[i] = row
        i = i + 1
