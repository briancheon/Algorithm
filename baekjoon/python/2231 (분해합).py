import sys

N = int(sys.stdin.readline().rstrip())

best = 0

for n in range(N):
    if n + sum(map(int, str(n))) == N:
        best = n
        break

print(best)
