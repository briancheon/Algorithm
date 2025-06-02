import sys
import heapq


N = int(sys.stdin.readline().rstrip())
C = []
for c in range(N):
    deck = int(sys.stdin.readline().rstrip())
    C.append(deck)

total = 0
heapq.heapify(C)

while len(C) > 1:
    n1 = heapq.heappop(C)
    n2 = heapq.heappop(C)
    total += n1 + n2
    heapq.heappush(C, n1 + n2)

print(total)

