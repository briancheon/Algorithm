import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)