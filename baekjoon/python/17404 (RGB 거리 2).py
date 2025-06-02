import sys

N = int(input().rstrip())
cost = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(min(cost[0]))

answer = float('inf')
for first in range(3):
    dp = [[float('inf')] * 3 for _ in range(N)]
    dp[0][first] = cost[0][first]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    
    for color in range(3):
        if color == first:
            continue
        answer = min(answer, dp[N - 1][color])

print(answer)
