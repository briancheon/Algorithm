import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N + 1)

dp[1] = dp[3] = 1

for i in range(4, N + 1):
    dp[i] = not (dp[i - 1] and dp[i - 3])
    
print("SK" if dp[N] else "CY")