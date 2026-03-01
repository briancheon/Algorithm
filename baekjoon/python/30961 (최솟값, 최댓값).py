import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

answer = A[0] * A[0]
for i in range(1, N):
    answer ^= A[i] * A[i]
    answer ^= A[i - 1] * A[i]

print(answer)