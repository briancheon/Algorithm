import sys
from collections import deque


def dfs(g, v):
    visited_dfs.add(v)
    print(v, end=' ')
    for i in g[v]:
        if i not in visited_dfs:
            dfs(g, i)
    
    
def bfs(g, v):
    q = deque([v])
    visited_bfs.add(v)
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in g[v]:
            if i not in visited_bfs:
                q.append(i)
                visited_bfs.add(i)
    


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
graph = list(map(sorted, graph))

visited_dfs = set()
visited_bfs = set()

dfs(graph, V)
print()
bfs(graph, V)