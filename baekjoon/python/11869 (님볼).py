import sys
from functools import reduce

M = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

result = reduce(lambda x, y: x ^ y, P)
print("koosaga" if result else "cubelover")