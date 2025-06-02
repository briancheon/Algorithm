import sys
from itertools import permutations


def s(string):
    return ' '.join(string)


N, M = map(int, sys.stdin.readline().split())
base = list("12345678"[:N])

perm = list(permutations(base, M))
answer = list(map(s, perm))

print(*answer, sep='\n')
