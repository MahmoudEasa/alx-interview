#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics

    Input format:
        <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
            <status code> <file size>
        (if the format is not this one, the line must be skipped)

    format: <status code>: <number>
"""
import sys
import re


def print_status(total_size, status_codes):
    """ Print Status Function """
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")


def read_stdin():
    """ Read Stdin Function """
    total_size = 0
    status_codes = {}
    counter = 0
    pattern = re.compile(r'\b^[0-9]+.[0-9]+.[0-9]+.[0-9]+ - '
                         r'\[[0-9]+-[0-9]+-[0-9]+ '
                         r'[0-9]+:[0-9]+:[0-9]+.[0-9]+\] '
                         r'"GET \/projects\/260 HTTP\/1.1" '
                         r'(200|301|400|401|403|404|405|500) ([0-9]+)$\b')

    try:
        for line in sys.stdin:
            counter += 1
            match = pattern.search(line)

            if not match:
                continue

            status_code = match.group(1)
            size = match.group(2)

            total_size += int(size)
            if not status_codes.get(status_code, None):
                status_codes[status_code] = 1
            else:
                status_codes[status_code] += 1

            if counter == 10:
                print_status(total_size, status_codes)
                counter = 0
                status_codes = {}
        print_status(total_size, status_codes)
    except KeyboardInterrupt:
        print_status(total_size, status_codes)


if __name__ == "__main__":
    read_stdin()
