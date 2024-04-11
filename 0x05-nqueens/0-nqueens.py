#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

n = int(sys.argv[1])


def solveNQueens(n):
    res = []
    cols = set()
    posd = set()
    negd = set()

    def backtrack(row, state):
        if row == n:
            res.append(state)
            return

        for col in range(n):
            po = row + col
            ne = row - col
            if col not in cols and po not in posd and ne not in negd:
                cols.add(col)
                posd.add(po)
                negd.add(ne)
                # Add queen to the state
                new_state = state + [[row, col]]
                # Recursively explore with the new state
                backtrack(row + 1, new_state)
                # Backtrack by removing the last queen placed
                cols.remove(col)
                posd.remove(po)
                negd.remove(ne)
    backtrack(0, [])
    return res


for sol in solveNQueens(n):
    print(sol)
