import sys

N, M = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().rstrip() for _ in range(N)]

a = len(list(filter(lambda x: "X" not in x, data)))
b = len(list(filter(lambda x: "X" not in x, [list(col) for col in zip(*data)])))

print(max(a, b))
