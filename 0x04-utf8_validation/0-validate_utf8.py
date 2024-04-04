#!/usr/bin/python3
""" UTF-8 Validation."""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8"""
    continuation_bytes = 0

    for byte in data:
        if continuation_bytes:
            if byte >> 6 != 0b10:
                return False
            continuation_bytes -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                continuation_bytes = 1
            elif byte >> 4 == 0b1110:
                continuation_bytes = 2
            elif byte >> 3 == 0b11110:
                continuation_bytes = 3
            else:
                return False

    return continuation_bytes == 0
