#!/usr/bin/env python3

import sys
import math

import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
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
        d = gcd(abs(x - y), n)
    return d

def factorize_number(n):
    if n == 1:
        return 1, 1
    if is_prime(n):
        return n, 1

    factor = pollards_rho(n)
    return factor, n // factor

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_file(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            number = int(line.strip())
            p, q = factorize_number(number)
            print(f"{number}={p}*{q}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    factorize_file(input_file)
