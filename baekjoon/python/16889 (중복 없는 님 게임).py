import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

G = [i for i in range(11) for j in range(i + 1)]

nim_sum = reduce(lambda x, y: x ^ y, [G[a] for a in A])
print("koosaga" if nim_sum else "cubelover")