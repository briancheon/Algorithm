import sys
from functools import reduce

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

N, A, B = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))

G = [0] * 1000001