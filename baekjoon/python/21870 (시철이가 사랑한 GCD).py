import sys
from functools import reduce
from math import floor, ceil

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_gcd(arr, n):
    if n == 1:
        return arr[0]
    
    left = arr[:n // 2]
    right = arr[n // 2:]
    
    return max(reduce(gcd, left) + max_gcd(right, ceil(n / 2)), max_gcd(left, floor(n / 2)) + reduce(gcd, right))

N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

print(max_gcd(a, N))