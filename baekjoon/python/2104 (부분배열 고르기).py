import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, input().split()))

A_cumulative_sum = [0] * (N + 1)
for i in range(1, N + 1) :
  A_cumulative_sum[i] = A_cumulative_sum[i - 1] + A[i - 1]

stack, max_interval = list(), 0

for i in range(N) :
  j = i
  while stack and stack[-1][0] >= A[i] :
    h, j = stack.pop()
    max_interval = max(max_interval, (A_cumulative_sum[i] - A_cumulative_sum[j]) * h)
  stack.append((A[i], j))

while stack :
  h, j = stack.pop()
  max_interval = max(max_interval, (A_cumulative_sum[-1] - A_cumulative_sum[j]) * h)

print(max_interval)