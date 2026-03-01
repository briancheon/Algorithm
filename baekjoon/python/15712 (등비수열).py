import sys

a, r, n, mod = map(int, sys.stdin.readline().split())


def fsum(ratio, p):
    if p == 1:
        return 1
    
    half = fsum(ratio, p // 2) % mod
    if p % 2:
        return 