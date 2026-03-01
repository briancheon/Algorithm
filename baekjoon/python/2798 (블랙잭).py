import sys

N, M = map(int, sys.stdin.readline().split())
_n = list(set(map(int, sys.stdin.readline().split())))

best = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            test = _n[i] + _n[j] + _n[k]
            if best < test <= M:
                best = test
            if best == M:
                break

print(best)

