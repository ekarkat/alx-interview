#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics: """

import sys


def print_msg(file_size, status_codes):
    """the print msg"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in texto:
        count += 1
        parts = line.split()
        try:
            if parts[-2] in status_codes.keys():
                status_codes[parts[-2]] += 1
            if parts[-1].isdigit:
                file_size += int(parts[-1])
        except Exception:
            pass
        if count % 10 == 0 and file_size != 0 and count != 0:
            print_msg(file_size, status_codes)
    print_msg(file_size, status_codes)


except KeyboardInterrupt:
    print_msg(file_size, status_codes)
