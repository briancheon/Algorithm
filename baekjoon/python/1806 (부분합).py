import sys

N, S = map(int, sys.stdin.readline().split())
ls = list(map(int, sys.stdin.readline().split()))

interval_sum, end = 0, 0
minimum_length = float('inf')

for start in range(N):
    while interval_sum < S and end < N:
        interval_sum += ls[end]
        end += 1
    
    if interval_sum >= S:
        minimum_length = min(minimum_length, end - start)
    
    interval_sum -= ls[start]

if minimum_length == float('inf'):
    print(0)
else:
    print(minimum_length)