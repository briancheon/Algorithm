import sys

MOD = 1000000007

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def fast_pow(n, k):
    if k == 1:
        return n
    
    half_pow = fast_pow(n, k // 2)
    if k % 2:
        return half_pow * half_pow * n % MOD
    else:
        return half_pow * half_pow % MOD
    
def comb(n, r):
    numerator = factorial(n) % MOD
    denominator = fast_pow(factorial(r) * factorial(n - r), MOD - 2) % MOD

    return numerator * denominator % MOD

dp = [0] * (K + 1)
dp[0] = N

for i in range(1, K + 1):
    temp = fast_pow(N + 1, i + 1) - 1
    for j in range(i):
        temp -= comb(i + 1, j) * dp[j]
		
    dp[i] = (temp % MOD) * fast_pow(comb(i + 1, i) , MOD - 2) % MOD

print(dp[K] % MOD)