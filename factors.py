#!/usr/bin/env python3

import sympy
import sys
import random
import math

def pollard_rho(n):
    if n % 2 == 0:
        return 2

    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1

    f = lambda x: (x**2 + c) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = sympy.gcd(abs(x-y), n)

    return d

def trial_division(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            return i
    return n

def quadratic_sieve(n):
    factors = sympy.factorint(n)
    return list(factors.keys())

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

        # Use Pollard's rho for larger factors
        while n > 1 and n < 100000000:
            factor = pollard_rho(n)
            factors.append(factor)
            n //= factor

        # Use Quadratic Sieve for even larger factors
        if n > 1:
            factors.extend(quadratic_sieve(n))

        factors_str = '*'.join(map(str, factors))
        print(f"{num}={factors_str}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize(file_path)
