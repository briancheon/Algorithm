import sys
import heapq

T = int(sys.stdin.readline().rstrip())

for c in range(T):
    N = int(sys.stdin.readline().rstrip())
    C = list(map(int, sys.stdin.readline().split()))
    total = 1
    heapq.heapify(C)

    while len(C) > 1:
        n1 = heapq.heappop(C)
        n2 = heapq.heappop(C)
        total *= n1 * n2
        heapq.heappush(C, n1 * n2)

    print(total % 1000000007)
