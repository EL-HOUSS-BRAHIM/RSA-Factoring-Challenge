#!/usr/bin/env python3

import math
from sympy import factorint

def factorize(n):
    return factorint(n)

def main():
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line)
            factors = factorize(n)
            for p, exp in factors.items():
                print(f"{n}={p}^{exp}")
                n //= p**exp

if __name__ == "__main__":
    main()
