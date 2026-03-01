import sys

N, Q = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

rotation = 0

for _ in range(Q):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] == 1:
        i, x = query[1], query[2]
        a[(i - 1 - rotation) % N] += x

    elif query[0] == 2:
        s = query[1]
        rotation = (rotation + s) % N
        
    elif query[0] == 3:
        s = query[1]
        rotation = (rotation - s) % N

if rotation:
    a = a[-rotation:] + a[:-rotation]

print(*a)