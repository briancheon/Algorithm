import sys

N = int(sys.stdin.readline().rstrip())

connection = [[] for _ in range(N + 1)]
dp = []

for c in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    connection[u].append(v)
    connection[v].append(u)


