#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics: """

import sys


def print_out(dic, size):
    """Print function"""
    print("File size: {}".format(size))
    for key in sorted(dic.keys()):
        if dic[key] != 0:
            print("{}: {}".format(key, dic[key]))


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        if len(parts) == 9:
            if parts[7].isdigit and parts[8].isdigit:
                try:
                    status_codes[parts[7]] += 1
                except Exception:
                    pass
                try:
                    file_size = file_size + int(parts[8])
                except Exception:
                    pass
        if count % 10 == 0:
            print_out(status_codes, file_size)

except KeyboardInterrupt:
    print_out(status_codes, file_size)
