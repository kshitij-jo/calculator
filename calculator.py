#!/usr/bin/env python

def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    import sys
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    print(multiply(first, second))
