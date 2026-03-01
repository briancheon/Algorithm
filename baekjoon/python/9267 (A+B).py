import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return 0, 1
    x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y

def solution(a, b, s):
    if a == 0 and b == 0:
        return s == 0
    
    if a == 0:
        return b != 0 and s % b == 0 and s // b >= 0
    
    if b == 0:
        return a != 0 and s % a == 0 and s // a >= 0

    d = gcd(a, b)
    if s % d != 0:
        return False
    a //= d; b //= d; s //= d

    x0, y0 = extended_gcd(a, b)
    x0 *= s
    y0 *= s

    n = x0 // b
    x0 -= n * b
    y0 += n * a

    while y0 >= 0:
        if x0 >= 0 and gcd(x0, y0) == 1:
            return True
        x0 += b
        y0 -= a

    return False

A, B, S = map(int, sys.stdin.readline().split())
print("YES" if solution(A, B, S) else "NO")