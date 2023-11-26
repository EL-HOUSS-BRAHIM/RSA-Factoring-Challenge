#!/usr/bin/python3

import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_keypair():
    p = random_prime()
    q = random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = modinv(e, phi)

    return ((e, n), (d, n))

def random_prime():
    while True:
        num = random.randrange(100, 1000)
        if is_prime(num):
            return num

def modinv(a, m):
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

if __name__ == "__main__":
    public_key, private_key = generate_keypair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)
