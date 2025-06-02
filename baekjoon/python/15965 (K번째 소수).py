import sys

K = int(sys.stdin.readline().rstrip())

limit = 7400001

primes = [1] * limit

for i in range(2, int(limit ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, limit, i):
            primes[j] = 0

final = [i for i in range(2, limit) if primes[i]]
print(final[K - 1])