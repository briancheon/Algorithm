import sys
from math import sqrt, ceil

def position(n):
    l = ceil((-1 + sqrt(1 + 8 * n)) / 2)
    return l, n - (l * (l - 1) // 2)

X = int(sys.stdin.readline().rstrip())

level, index = position(X)

if level % 2:
    numerator, denominator = level - index + 1, index

else:
    numerator, denominator = index, level - index + 1

print(f'{numerator}/{denominator}')

