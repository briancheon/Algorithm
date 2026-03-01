import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

dp_increase = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

dp_decrease = [1] * N
for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if A[j] < A[i]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

max_length = 0
for i in range(N):
    if dp_increase[i] + dp_decrease[i] - 1 > max_length:
        max_length = dp_increase[i] + dp_decrease[i] - 1
            
print(max_length)