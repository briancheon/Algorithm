import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().rstrip())
    in_out = 0
    for c in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        distance1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
        distance2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5

        if (distance1 <= r) ^ (distance2 <= r):
            in_out += 1

    print(in_out)
