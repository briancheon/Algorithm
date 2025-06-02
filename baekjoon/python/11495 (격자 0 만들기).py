import sys

T = int(sys.stdin.readline().rstrip())

# chess

for c in range(T):
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        grid.append(row)
