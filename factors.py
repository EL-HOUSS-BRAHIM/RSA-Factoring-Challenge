#!/usr/bin/env python3


import sympy
import sys
import random

def ecm_factorization(n):
    factors = sympy.ecm.factor(n, B1=100, sigma=1)
    return factors

def trial_division(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            return i
    return n

def factorize(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        n = int(num)
        factors = []

        # Use trial division for small factors
        while n > 1 and n < 1000000:
            factor = trial_division(n)
            factors.append(factor)
            n //= factor

        # Use ECM for larger factors
        if n > 1:
            factors.extend(ecm_factorization(n))

        factors_str = '*'.join(map(str, factors))
        print(f"{num}={factors_str}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize(file_path)
