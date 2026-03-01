import sys
from bisect import bisect_left

N, Q = map(int, sys.stdin.readline().split())
A = sorted(map(int, sys.stdin.readline().split()))

idx_memo = {}
min_max = [None] * 300001
for m in range(1, 300001):
    minimum, maximum = m - 1, 0
    for x in range((A[0] // m) * m, A[-1] + 1, m):
        if x not in idx_memo:
            idx = bisect_left(A, x)
            idx_memo[x] = idx
        
        idx = idx_memo[x]
        left = A[idx - 1] % m
        right = A[idx] % m if idx < N else left

        minimum = min(minimum, left, right)
        maximum = max(maximum, left, right)

    min_max[m] = (minimum, maximum)

for _ in range(Q):
    m = int(sys.stdin.readline().rstrip())
    print(*min_max[m])