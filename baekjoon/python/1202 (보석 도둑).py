import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline().strip()) for _ in range(K)]

jewels.sort()
bags.sort()

max_price = 0
heap = []
i = 0

for capacity in bags:
    while i < N and jewels[i][0] <= capacity:
        heapq.heappush(heap, -jewels[i][1])
        i += 1
    
    if heap:
        max_price += -heapq.heappop(heap)

print(max_price)