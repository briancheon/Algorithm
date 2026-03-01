import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

q = deque([(A, 1)])
possible = False
visited = set()

while q:
    cur, cnt = q.popleft()
    if cur == B:
        possible = True
        break
    
    for next_num in [cur * 2, cur * 10 + 1]:
        if next_num <= B and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, cnt + 1))
            
print(cnt if possible else -1)