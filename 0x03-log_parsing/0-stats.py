#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics: """

import sys


def print_out(dic, size):
    """Print function"""
    print("File size: {}".format(size))
    for key, value in sorted(dic.items()):
        if dic[key] != 0:
            print("{}: {}".format(key, value))


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        try:
            if parts[-2] in status_codes.keys():
                status_codes[parts[-2]] += 1
        except Exception:
            pass
        try:
            file_size = file_size + int(parts[-1])
        except Exception:
            pass
        if count % 10 == 0:
            print_out(status_codes, file_size)

except KeyboardInterrupt:
    print_out(status_codes, file_size)
