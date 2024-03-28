#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics: """

import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        parts = line.split()
        try:
            if parts[-2] in status_codes.keys() and parts[-1].isdigit:
                status_codes[parts[-2]] += 1
                file_size = file_size + int(parts[-1])
        except Exception:
            pass
        if count % 10 == 0 and file_size != 0 and count != 0:
            print("File size: {}".format(file_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))

except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
