import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

visited = set()
prev = {N: -1}
q = deque([N])

while q:
    cur = q.popleft()
    if cur == K:
        path = []
        while cur != N:
            path.append(cur)
            cur = prev[cur]
        
        print(len(path))
        path.append(N)
        print(*path[::-1])
        break
    
    for next_pos in (cur - 1, cur + 1, 2 * cur):
        if 0 <= next_pos <= 100000 and next_pos not in visited:
            visited.add(next_pos)
            prev[next_pos] = cur
            q.append(next_pos)