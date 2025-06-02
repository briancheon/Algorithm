import sys
from functools import reduce

N, M = map(int, sys.stdin.readline().split())
grid = [sum(map(int, sys.stdin.readline().split())) for _ in range(N)]

nim_sum = reduce(lambda x, y: x ^ y, grid)
print("august14" if nim_sum else "ainta")