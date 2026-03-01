import sys
from collections import deque, defaultdict

def bfs(graph, start):
    q = deque([start])
    visited = {start}

    while q:
        cur = q.popleft()

        for next_node in graph[cur]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)

    return visited

N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(set)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].add(v)
    graph[v].add(u)

nodes = set(range(1, N + 1))
cnt = 0
while nodes:
    node = nodes.pop()
    nodes -= bfs(graph, node)
    cnt += 1

print(cnt)