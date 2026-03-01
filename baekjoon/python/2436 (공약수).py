import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return B


def lcm(a, b):
    return a * b // gcd(a, b)


A, B = map(int, sys.stdin.readline().split())

print(gcd(A, B), lcm(A, B))