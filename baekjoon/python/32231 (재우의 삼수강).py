import sys
from math import log, atan2, tan

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    
    if x1 == x2:
        print(abs(log(y2 / y1)))
        continue

    if x1 > x2:
        x1, x2 = x2, x1

    if y1 > y2:
        y1, y2 = y2, y1

    C = (x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1) / (2 * (x2 - x1))

    theta1 = atan2(y1, x1 - C)
    theta2 = atan2(y2, x2 - C)

    print(abs(log(tan(theta2 / 2) / tan(theta1 / 2))))
