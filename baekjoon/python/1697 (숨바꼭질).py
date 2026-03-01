import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dp = [0] * 100001

q = deque([N])
cnt = 0

while q:
    pos = q.popleft()
    if pos == K:
        cnt += 1
        continue
    
    for next_pos in (pos - 1, pos + 1, 2 * pos):
        if 0 <= next_pos <= 100000 and (not dp[next_pos] or dp[next_pos] == dp[pos] + 1):
            dp[next_pos] = dp[pos] + 1
            q.append(next_pos)
            
print(dp[K])
print(cnt)