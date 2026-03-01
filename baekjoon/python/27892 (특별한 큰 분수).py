import sys

x0, N = map(int, sys.stdin.readline().split())

for _ in range(N):
    if x0 % 2 == 0:
        x0 = (x0 // 2) ^ 6

    else:
        x0 = (x0 * 2) ^ 6

print(x0)
