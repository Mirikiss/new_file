import sys
from seminar_6 import find_number


if __name__ == '__main':
    options = list(map(int, sys.argv[1:]))
    low_nmb = 1
    high_num = 100
    counter = 5
    if len(options) == 1:
        high_num = options
    elif len(options) == 2:
        low_nmb, high_num = options
    else:
        low_nmb, high_num, counter, *_ = options
find_number(low_nmb, high_num, counter)
