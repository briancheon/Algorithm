import sys

MOD = 1000000007

def fast_pow(n, k):
    if k == 1:
        return n
    
    half_pow = fast_pow(n, k // 2)
    if k % 2:
        return half_pow * half_pow * n
    else:
        return half_pow * half_pow

N, p = map(int, sys.stdin.readline().split())

pascal_triangle = [[1] * (p + 2) for _ in range(p + 2)]
for i in range(1, p + 2):
    for j in range(1, i):
        pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

dp = [0] * (p + 1)
dp[0] = N

for i in range(1, p + 1):
    temp = fast_pow(N + 1, i + 1) - 1
    for j in range(i):
        temp -= pascal_triangle[i + 1][j] * dp[j]
		
    dp[i] = temp // (i + 1)

print(dp[p] % MOD)