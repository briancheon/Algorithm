import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dp = [0] * 100001
visited = [0] * 100001

q = deque([N])
cnt = 0

while q:
    pos = q.popleft()
    if pos == K:
        print(dp[pos])
        break
    
    next_pos = 2 * pos
    if 0 <= next_pos <= 100000 and not visited[next_pos]:
            dp[next_pos] = dp[pos]
            q.append(next_pos)
            visited[next_pos] = 1
    
    for next_pos in (pos - 1, pos + 1):
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            dp[next_pos] = dp[pos] + 1
            q.append(next_pos)
            visited[next_pos] = 1
    
    