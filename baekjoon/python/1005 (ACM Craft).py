import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[X].append(Y)
        indegree[Y] += 1

    W = int(sys.stdin.readline().rstrip())

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            dp[i] = max(dp[cur] + D[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[W])