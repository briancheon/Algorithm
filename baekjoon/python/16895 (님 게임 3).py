import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

nim_sum = reduce(lambda x, y: x ^ y, P)

cnt = len(list(filter(lambda x: x ^ nim_sum < x, P)))

print(cnt)