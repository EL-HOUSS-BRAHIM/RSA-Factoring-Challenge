#!/usr/bin/env python3

import sys

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    x = 2
    y = 2
    d = 1

    while d == 1:
        x = (x * x + 1) % n
        y = (y * y + 1) % n
        y = (y * y + 1) % n
        d = gcd(abs(x - y), n)

    return d

def factorize(n):
    if n == 1:
        return []

    factors = []
    while n > 1:
        p = pollard_rho(n)
        factors.append(p)
        n //= p

    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for line in f:
            n = int(line)
            factors = factorize(n)
            print(f"{n} = {' * '.join(map(str, factors))}")

if __name__ == "__main__":
    main()
