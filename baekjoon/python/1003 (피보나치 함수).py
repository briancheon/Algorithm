import sys

ls = [[1, 0], [0, 1]] + [[0, 0]] * 39
for c in range(2, 41):
    ls[c] = list(map(lambda x, y: x + y, ls[c - 1], ls[c - 2]))

T = int(sys.stdin.readline().rstrip())

for c in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(*ls[N])
