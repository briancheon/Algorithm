from collections import defaultdict
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().split()))

_nums = defaultdict(int)
for a in A:
    _nums[a] = 1

for c in check:
    print(_nums[c])
