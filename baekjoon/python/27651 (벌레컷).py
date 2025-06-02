import sys
import bisect

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N + 1)
for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + A[i]

cnt = 0

for i in range(1, N - 1):
    head = prefix_sum[i]
    chest = (prefix_sum[-1] + head) / 2
    stomach = prefix_sum[-1] - head
    
    left = bisect.bisect_right(prefix_sum, chest, lo=i + 1, hi=N)
    right = bisect.bisect_left(prefix_sum, stomach, lo=i + 1, hi=N) - 1
    
    if left <= right and left <= N - 1 and right >= i + 1:
        cnt += (right - left + 1)

print(cnt)