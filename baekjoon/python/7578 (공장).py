import sys

N = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

counts = [0] * N

for c in range(N):
    counts[c] = abs(c - B.index(A[c]))

print(counts)
