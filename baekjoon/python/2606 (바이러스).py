import sys
from collections import deque
from collections import defaultdict

def bfs(graph, start):
    cnt = 0
    q = deque([start])
    visited = {start}

    while q:
        cur = q.popleft()

        for next_node in graph[cur]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)
                cnt += 1

    return cnt

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

computers = defaultdict(set)
for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())
    computers[c1].add(c2)
    computers[c2].add(c1)

print(bfs(computers, 1))