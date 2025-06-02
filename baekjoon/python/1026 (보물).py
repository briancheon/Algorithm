import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

total = 0
A = sorted(A)
B = sorted(B, reverse=True)
for c in range(N):
    total += A[c] * B[c]

print(total)
