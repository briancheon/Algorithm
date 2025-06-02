import sys

MOD = 1000000007

def fpow(C, n):
    if n == 0:
        return 1
    
    half = fpow(C, n // 2)
    
    if n % 2 == 0:
        return half * half % MOD
    else:
        return half * half * C % MOD


factorials = [1] * 4000001
for i in range(1, 4000001):
    factorials[i] = factorials[i - 1] * i % MOD


M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    N, K = map(int, sys.stdin.readline().split())
    denominator = (factorials[K] * factorials[N - K]) % MOD
    print(factorials[N] * fpow(denominator, MOD - 2) % MOD)