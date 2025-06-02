import sys

A, B, N = map(int, sys.stdin.readline().split())

n_A, dp = A % B, 0

for c in range(N):
    n_A *= 10
    dp = n_A // B
    n_A %= B
    if n_A == 0:

        break

print(dp)
