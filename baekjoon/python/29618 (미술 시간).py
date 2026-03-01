import sys

N, Q = map(int, sys.stdin.readline().split())

values = list(range(1, N + 1))
updated = [False] * N
queries = []

for _ in range(Q):
    a, b, x = map(int, sys.stdin.readline().split())
    queries.append((a-1, b-1, x))

for a, b, x in reversed(queries):
    for j in range(a, b + 1):
        if not updated[j]:
            values[j] = x
            updated[j] = True

print(' '.join(map(str, values)))