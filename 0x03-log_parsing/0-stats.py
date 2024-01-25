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
    for code, count in status_codes.items():
        if count > 0:
            print(f"{code}: {count}")


def match_input(input_line):
    """ Check if input line match """
    data = {'status_code': 0, 'file_size': 0}

    pattern = re.compile(r'\b^[0-9]+.[0-9]+.[0-9]+.[0-9]+ - '
                         r'\[[0-9]+-[0-9]+-[0-9]+ '
                         r'[0-9]+:[0-9]+:[0-9]+.[0-9]+\] '
                         r'"GET \/projects\/260 HTTP\/1.1" '
                         r'(200|301|400|401|403|404|405|500) ([0-9]+)$\b')

    match = pattern.search(input_line)
    if not match:
        return (None)

    data['status_code'] = int(match.group(1))
    data['file_size'] = int(match.group(2))
    return (data)


def main():
    """ Main Function """
    total_size = 0
    status_codes = {
                200: 0,
                301: 0,
                400: 0,
                401: 0,
                403: 0,
                404: 0,
                405: 0,
                500: 0
            }
    counter = 0

    try:
        for line in sys.stdin:
            data = match_input(line)
            counter += 1

            if not data:
                continue

            status_code = data['status_code']

            if status_code not in status_codes:
                continue

            total_size += data['file_size']
            status_codes[status_code] += 1

            if counter % 10 == 0:
                print_status(total_size, status_codes)
        print_status(total_size, status_codes)
    except KeyboardInterrupt:
        print_status(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
