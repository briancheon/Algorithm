import sys

INF = int(1e9)

N = int(sys.stdin.readline().rstrip())
VISITED_ALL = (1 << N) - 1

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(cur, visited, distances):
    if visited == VISITED_ALL:
        if not distances[cur][0]:
            return INF
        dp[cur][visited] = distances[cur][0]
        return cost[cur][0]

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    min_length = INF
    for i in range(N):
        if distances[cur][i] and not (visited & (1 << i)):
            length = tsp(i, visited | (1 << i), distances) + distances[cur][i]
            min_length = min(min_length, length)

    dp[cur][visited] = min_length
    return min_length

cost = []

for _ in range(N):
    cost.append(list(map(int, sys.stdin.readline().split())))

print(tsp(0, 1, cost))
