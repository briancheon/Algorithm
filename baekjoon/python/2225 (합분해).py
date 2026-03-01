import sys

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def nHr(n, r):
    return factorial(n + r - 1) // (factorial(r) * factorial(n - 1))


N, K = map(int, sys.stdin.readline().split())

print(nHr(K, N) % 1000000000)
