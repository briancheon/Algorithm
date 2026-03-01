import sys

N = int(sys.stdin.readline().rstrip())
_n = {}
for c in range(N):
    _n[c + 1] = (list(map(int, sys.stdin.readline().split())))

print(_n)
_x = sorted(_n.items(), key=lambda x: x[1][0])
_y = sorted(_n.items(), key=lambda x: x[1][1])
print(_x)
print(_y)
