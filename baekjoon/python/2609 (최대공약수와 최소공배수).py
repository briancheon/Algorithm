import sys

def gcd(n, m):
    while m:
        n, m = m, n % m

    return n

def lcm(n, m):
    return n * m // gcd(n, m)

N, M = map(int, sys.stdin.readline().split())
print(gcd(N, M))
print(lcm(N, M))
