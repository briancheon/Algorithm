import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    q = deque((i, idx) for idx, i in enumerate(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    
    while True:
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            cnt += 1
            if q[0][1] == M:
                print(cnt)
                break
            q.popleft()
        else:
            q.append(q.popleft())
        
