import sys

N, M = map(int, sys.stdin.readline().split())

_index = list(map(int, sys.stdin.readline().split()))

q = list(range(1, N + 1))

count = 0

for i in _index:
    idx = q.index(i)
    if idx < N / 2:
        q = q[idx + 1:] + q[:idx]
        count += idx

    else:
        q = q[idx + 1:] + q[:idx]
        count += N - idx

    N -= 1

print(count)
