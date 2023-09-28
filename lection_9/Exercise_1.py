from typing import Callable

def main(x: int):
    d = {}

    def loc(y: int):
        for i in range(y):
            d[i] = x ** i
        return d

    return loc

small = main(42)
big = main(73)
print(small(7), big(7), small(3), sep = '\n')