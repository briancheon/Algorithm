import sys
from collections import deque

class Pos:
    def __init__(self, x, y, z, d):
        self.x = x
        self.y = y
        self.z = z
        self.d = d

_x, _y, _z = [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1], [1, -1, 0, 0, 0, 0]

M, N, H = map(int, sys.stdin.readline().split())
index = 3
tomatoes = []
q = deque()
unripe_count = 0

for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        index += M
        layer.append(row)
        for m in range(M):
            if row[m] == 1:
                q.append(Pos(n, m, h, 0))
            elif row[m] == 0:
                unripe_count += 1
    tomatoes.append(layer)

max_days = 0
while q:
    cur = q.popleft()
    for c in range(6):
        nx, ny, nz = cur.x + _x[c], cur.y + _y[c], cur.z + _z[c]
        nd = cur.d + 1

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and tomatoes[nz][nx][ny] == 0:
            tomatoes[nz][nx][ny] = 1
            q.append(Pos(nx, ny, nz, nd))
            unripe_count -= 1
            max_days = nd

if unripe_count > 0:
    print(-1)
else:
    print(max_days)