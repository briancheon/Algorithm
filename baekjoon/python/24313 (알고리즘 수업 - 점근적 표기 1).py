import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

if c * n0 >= a1 * n0 + a0 and c >= a1:
    print(1)
else:
    print(0)
