import sys


N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A = list(filter(lambda x: x < X, A))
print(*A, sep=' ')
