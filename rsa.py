#!/usr/bin/env python3

import sys
import math

from factors import factorize_number

def rsa_factorize_number(n):
    """
    Factorize an RSA number into a product of two prime numbers.

    :param n: The RSA number to factorize.
    :return: A tuple (p, q) where p * q = n, and p and q are prime.
    """
    p, q = factorize_number(n)
    while not (is_prime(p) and is_prime(q)):
        p, q = factorize_number(n)
    return p, q

def is_prime(num):
    """
    Check if a number is prime.

    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def rsa_factorize_file(input_file):
    """
    Factorize RSA numbers from a file and print the factorization.

    :param input_file: The file containing RSA numbers to factor.
    """
    with open(input_file, 'r') as file:
        for line in file:
            rsa_number = int(line.strip())
            p, q = rsa_factorize_number(rsa_number)
            print(f"{rsa_number}={p}*{q}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    rsa_factorize_file(input_file)
