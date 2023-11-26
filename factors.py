#!/usr/bin/env python3

import sys
import math

def factorize_number(n):
    """
    Factorize a number into a product of two smaller numbers.

    :param n: The number to factorize.
    :return: A tuple (p, q) where p * q = n.
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def factorize_file(input_file):
    """
    Factorize numbers from a file and print the factorization.

    :param input_file: The file containing natural numbers to factor.
    """
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
