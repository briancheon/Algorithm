import sys

nA, nB = map(int, sys.stdin.readline().split())
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

diff = A - B

if diff:
    print(len(diff))
    print(*sorted(diff))
else:
    print(0)