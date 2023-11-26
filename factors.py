#!/usr/bin/env python3

import sys
import random

def gauss(M):
    marks = [False] * len(M)
    for j in range(len(M[0])):
        for i in range(len(M)):
            if M[i][j] == 1:
                marks[i] = True
                for k in range(j):
                    if M[i][k] == 1:
                        for row in range(len(M)):
                            M[row][k] = (M[row][k] + M[row][j]) % 2
                for k in range(j+1, len(M[0])):
                    if M[i][k] == 1:
                        for row in range(len(M)):
                            M[row][k] = (M[row][k] + M[row][j]) % 2
                break
    return (marks, M)

def get_dep_cols(row):
    ret = []
    for i in range(len(row)):
        if row[i] == 1:
            ret.append(i)
    return ret

def row_add(new_row, current):
    ret = current
    for i in range(len(M[new_row])):
        ret[i] ^= M[new_row][i]
    return ret

def is_dependent(cols, row):
    for i in cols:
        if row[i] == 1:
            return True
    return False

def find_linear_deps(row):
    ret = []
    dep_cols = get_dep_cols(M[row])
    current_rows = [row]
    current_sum = M[row][:]
    for i in range(len(M)):
        if i == row:
            continue
        if is_dependent(dep_cols, M[i]):
            current_rows.append(i)
            current_sum = row_add(i, current_sum)
        if sum(current_sum) == 0:
            ret.append(current_rows[:])
    return ret

def testdep(dep):
    x = y = 1
    for row in dep:
        x *= smooth_vals[row][0]
        y *= smooth_vals[row][1]
    return xgcd(x - isqrt(y), N)[0]

def phi(p):
    return p-1

def legendre(a, p):
    if a % p == 0:
        return 0
    return pow(a, (p - 1) // 2, p)

def miller(n, trials=5):
    s = 0
    d = n - 1
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    for _ in range(trials):
        a = random.randrange(2, n)
        composite = True
        if pow(a, d, n) == 1:
            continue
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                composite = False
                break
        if composite:
            return False
    return True

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def xgcd(a,b):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q, r = divmod(a,b)
        x, prevx = prevx - q*x, x
