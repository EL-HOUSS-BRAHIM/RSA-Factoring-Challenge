#!/usr/bin/env python3

# factors.py

import sympy
import sys

def factorize(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        n = int(num)
        factors = sympy.factorint(n)
        factors_str = '*'.join([f"{factor}**{exponent}" for factor, exponent in factors.items()])
        print(f"{num}={factors_str}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize(file_path)
