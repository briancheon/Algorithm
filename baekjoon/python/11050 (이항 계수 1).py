import sys

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact

N, K = map(int, sys.stdin.readline().split())

print(factorial(N) // (factorial(K) * factorial(N - K)))
