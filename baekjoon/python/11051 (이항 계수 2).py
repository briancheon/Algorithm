import sys

MOD = 10007

def fpow(C, n):
    if n == 0:
        return 1
    
    half = fpow(C, n // 2)
    
    if n % 2 == 0:
        return half * half % MOD
    else:
        return half * half * C % MOD


def factorial(n):
    i = 1
    for j in range(1, n + 1):
        i *= j
        i %= MOD
    return i


N, K = map(int, sys.stdin.readline().split())
denominator = (factorial(K) * factorial(N - K)) % MOD
print(factorial(N) * fpow(denominator, MOD - 2) % MOD)