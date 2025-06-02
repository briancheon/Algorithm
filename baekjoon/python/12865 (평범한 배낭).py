import sys

dp = [[0] * 100001 for _ in range(101)]

N, K = map(int, sys.stdin.readline().split())
weight_value = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
	
for i in range(1, N + 1):
      for j in range(1, K + 1):
        if j < weight_value[i - 1][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - weight_value[i - 1][0]] + weight_value[i - 1][1], dp[i - 1][j])

print(dp[N][K])