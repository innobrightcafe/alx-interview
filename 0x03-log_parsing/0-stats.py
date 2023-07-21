#!/usr/bin/python3
import sys
import signal

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
file_sizes = []
lines_count = 0
status_count = {}

def print_statistics(signal, frame):
    global file_sizes, lines_count, status_count

    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    for status_code in sorted(status_count.keys()):
        if status_code in status_codes:
            print(f"{status_code}: {status_count[status_code]}")

    file_sizes = []
    lines_count = 0
    status_count = {}

signal.signal(signal.SIGINT, print_statistics)

for line in sys.stdin:
    try:
        _, _, _, status_code, file_size = line.strip().split(' ')
        status_code = int(status_code)
        file_size = int(file_size)

        if status_code in status_codes:
            file_sizes.append(file_size)
            lines_count += 1
            status_count[status_code] = status_count.get(status_code, 0) + 1
    except ValueError:
        # Skip the line if it doesn't match the input format
        continue

    if lines_count == 10:
        print_statistics(None, None)
