import sys
from collections import deque

class Pos:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

_x, _y = [0, 0, 1, -1], [1, -1, 0, 0]

M, N = map(int, sys.stdin.readline().split())
tomatoes = []
q = deque()
unripe_count = 0

for n in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    tomatoes.append(row)
    for m in range(M):
        if row[m] == 1:
            q.append(Pos(n, m, 0))
        elif row[m] == 0:
            unripe_count += 1

max_days = 0
while q:
    cur = q.popleft()
    for c in range(4):
        nx, ny = cur.x + _x[c], cur.y + _y[c]
        nd = cur.d + 1

        if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
            tomatoes[nx][ny] = 1
            q.append(Pos(nx, ny, nd))
            unripe_count -= 1
            max_days = nd

if unripe_count > 0:
    print(-1)
else:
    print(max_days)