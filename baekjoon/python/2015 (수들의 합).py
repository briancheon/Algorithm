import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N + 1)
prefix_sum[1] = A[0]

for i in range(2, N):
    prefix_sum[i] += prefix_sum[i - 1]

print(prefix_sum)
cnt = 0
for i in range(1, N + 1):
    for j in range(i):
        if prefix_sum[i] - prefix_sum[j] == K:
            cnt += 1

print(cnt)