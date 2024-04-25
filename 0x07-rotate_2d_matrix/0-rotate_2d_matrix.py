#!/usr/bin/python3
""" 2DMatrix Rotate"""


def rotate_2d_matrix(matrix):
    """ Matrix Rotater """
    n = len(matrix)
    cmat = [[0] * n for _ in range(n)]
    for i in range(len(cmat)):
        for j in range(len(cmat[i])):
            cmat[i][j] = matrix[len(cmat) - j - 1][i]
    i = 0
    for row in cmat:
        matrix[i] = row
        i = i + 1
