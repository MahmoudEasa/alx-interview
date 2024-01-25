#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


def print_stats(f_size, status_dict):
    """prints the log stats"""
    print('File size: {}'.format(f_size))
    for key, val in status_dict.items():
        if val:
            print('{}: {}'.format(key, val))


try:
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    file_size = 0
    counter = 0

    for line in sys.stdin:
        elements = line.split(' ')
        counter += 1

        try:
            stat_code = int(elements[-2])
            if stat_code not in status_codes:
                continue
        except Exception:
            continue

        try:
            size = int(elements[-1])
            file_size += size
        except Exception:
            continue

        status_codes[stat_code] += 1

        if counter == 10:
            print_stats(file_size, status_codes)
            counter = 0
    print_stats(file_size, status_codes)

except KeyboardInterrupt:
    print_stats(file_size, status_codes)
    raise
