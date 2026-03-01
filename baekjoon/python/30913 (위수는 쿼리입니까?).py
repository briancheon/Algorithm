import sys

N = int(sys.stdin.readline().rstrip())
Q = int(sys.stdin.readline().rstrip())

for _ in range(Q):
    query = list(map(int, sys.stdin.readline().rstrip()))

    if query[0] == 1:
        a = query[1]

    else:
        e = query[1]