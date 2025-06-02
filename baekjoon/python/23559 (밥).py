import sys
import heapq

N, X = map(int, sys.stdin.readline().split())
taste = []
satisfaction = 0

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    satisfaction += B
    taste.append(B - A)

heapq.heapify(taste)

X -= 1000 * N

while X >= 4000:
    t = heapq.heappop(taste)
    if t < 0:
        satisfaction -= t
        X -= 4000
    else:
        break
        
print(satisfaction)
