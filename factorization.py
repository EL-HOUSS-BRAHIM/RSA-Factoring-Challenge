#!/usr/bin/env python3
import sys

def prime_factorization(n):
    if n <= 3:
        return [int(n)]
    
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    
    i = 5
    w = 2
    
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += w
            w = 6 - w
    
    if n > 1:
        factors.append(n)
    
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factorization.py <number>")
        sys.exit(1)

    number = int(sys.argv[1])
    result = prime_factorization(number)
    print(result)
