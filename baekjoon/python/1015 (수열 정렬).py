import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))

A = sorted(enumerate(A), key=lambda x: x[1])

A = sorted(enumerate(A), key=lambda x: x[1])

for i in range(N):
    print(A[i][0], end=' ')
