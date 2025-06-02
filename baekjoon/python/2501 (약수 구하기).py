import sys

N, K = map(int, sys.stdin.readline().split())

factors = []

for n in range(1, N + 1):
    if N % n == 0:
        factors.append(n)

if K > len(factors):
    print(0)
else:
    print(factors[K - 1])
