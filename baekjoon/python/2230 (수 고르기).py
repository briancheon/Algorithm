import sys

N, M = map(int, sys.stdin.readline().split())
A = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])

l, r = 0, 0
min_diff = float('inf')

while l < N and r < N:
    if A[r] - A[l] == M:
        print(M)
        exit()
    elif A[r] - A[l] < M:
        r += 1
    else:
        min_diff = min(min_diff, A[r] - A[l])
        l += 1

print(min_diff)


        