import sys
from itertools import product


def s(string):
    return ' '.join(string)


N, M = map(int, sys.stdin.readline().split())
base = list("12345678"[:N])

p = product(base, repeat=M)
answer = list(map(s, p))

print(*answer, sep='\n')
