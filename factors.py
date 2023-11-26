#!/usr/bin/env python3

import math

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x-y), n)
    return d

def factorize(n):
    factors = []
    while n > 1:
        d = pollards_rho(n)
        factors.append(d)
        n //= d
    return factors

def main():
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    with open(sys.argv[1], 'r') as f:
        for line in f:
            n = int(line)
            factors = factorize(n)
            for p in factors:
                print(f"{n}={p}*{n//p}")
                n //= p

if __name__ == "__main__":
    main()
