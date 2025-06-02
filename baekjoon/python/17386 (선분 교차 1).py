import sys

def ccw(x1, y1, x2, y2, x3, y3):
    l1 = (x2 - x1, y2 - y1)
    l2 = (x3 - x2, y3 - y2)

    cross = l1[0] * l2[1] - l1[1] * l2[0]

    if cross < 0:
        return -1
    elif cross == 0:
        return 0
    else:
        return 1

def on_segment(x1, y1, x2, y2, x, y):
    return min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)

a1, b1, a2, b2 = map(int, sys.stdin.readline().split())
a3, b3, a4, b4 = map(int, sys.stdin.readline().split())

check1 = ccw(a1, b1, a2, b2, a3, b3)
check2 = ccw(a1, b1, a2, b2, a4, b4)

check3 = ccw(a3, b3, a4, b4, a1, b1)
check4 = ccw(a3, b3, a4, b4, a2, b2)

if check1 * check2 < 0 and check3 * check4 < 0:
    print(1)
elif check1 * check2 * check3 * check4 == 0 and on_segment(a1, b1, a2, b2, a3, b3):
    print(1)
else:
    print(0)
