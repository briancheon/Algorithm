import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
x = list(map(int, sys.stdin.readline().split()))

q = []
i, cur_sat = 0, 0
cnt = 0

for i in range(N):
    heapq.heappush(q, -x[i])
    cur_sat += x[i]
    while cur_sat >= M:
        biggest = -heapq.heappop(q)
        cur_sat -= 2 * biggest
        cnt += 1
    
print(cnt)
    