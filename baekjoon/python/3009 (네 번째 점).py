import sys

_x, _y = [], []

for c in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x not in _x:
        _x.append(x)
    else:
        _x.remove(x)
    if y not in _y:
        _y.append(y)
    else:
        _y.remove(y)

print(_x[0], _y[0])
