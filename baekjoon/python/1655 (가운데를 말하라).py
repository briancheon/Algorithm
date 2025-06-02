import sys
import heapq

N = int(sys.stdin.readline().rstrip())

left, right = [], []

for c in range(N):
    n = int(sys.stdin.readline().rstrip())
    if len(left) == len(right):
        heapq.heappush(left, -n)
    else:
        heapq.heappush(right, n)

    if right and right[0] < -left[0]:
        l_temp = heapq.heappop(left)
        r_temp = heapq.heappop(right)

        heapq.heappush(right, -l_temp)
        heapq.heappush(left, -r_temp)

    print(-left[0])






