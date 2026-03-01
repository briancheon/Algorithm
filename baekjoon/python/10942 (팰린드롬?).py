
import sys

N = int(sys.stdin.readline().rstrip())
nums = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 1

for i in range(1, N):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for length in range(3, N + 1):
    for s in range(1, N - length + 2):
        e = s + length - 1
        if nums[s] == nums[e] and dp[s + 1][e - 1]:
            dp[s][e] = 1

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(dp[S][E])