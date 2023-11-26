#!/usr/bin/env python3

import math
import sys

def factorize_number(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            n = int(line.strip())
            factors = factorize_number(n)
            print(f'{n}={factors[0]}*{factors[1]}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
