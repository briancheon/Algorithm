import sys

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())
VISITED_ALL = (1 << N) - 1

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(cur, visited):
    if visited == VISITED_ALL:
        if not cost[cur][0]:
            return INF
        dp[cur][visited] = cost[cur][0]
        return cost[cur][0]

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    min_length = INF
    for i in range(N):
        if cost[cur][i] and not (visited & (1 << i)):
            length = tsp(i, visited | (1 << i)) + cost[cur][i]
            min_length = min(min_length, length)

    dp[cur][visited] = min_length
    return min_length

points = []
cost = []

for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))

for x1, y1 in points:
    c = []
    for x2, y2 in points:
        c.append(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)
    cost.append(c)

print(tsp(0, 1))
