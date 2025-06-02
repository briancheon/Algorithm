import sys

def manhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

N, K = map(int, sys.stdin.readline().split())

checkpoints = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[float('inf')] * (K + 1) for _ in range(N)]
dp[0][0] = 0

for i in range(N):
    for k in range(K + 1):
        cur = dp[i][k]
        if cur == float('inf'):
            continue

        for j in range(i + 1, N):
            skip = k + j - i - 1
            if skip > K:
                continue
            dp[j][skip] = min(dp[j][skip], cur + manhattan(checkpoints[i], checkpoints[j]))

print(min(dp[N - 1]))