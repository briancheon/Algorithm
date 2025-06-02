"""
G(0) = 0
G(1) = mex({G(0)}) = mex({0}) = 1
G(2) = 0
G(3) = mex({G(0), G(1)}) = mex({0, 1}) = 2
G(4) = mex({G(2)}) = mex({0}) = 1
G(5) = mex({G(0), G(1), G(3)}) = mex({0, 1, 2}) = 3
G(6) = mex({G(2), G(4)}) = mex({0, 1}) = 2
G(7) = mex({G(0), G(1), G(3), G(5)}) = mex({0, 1, 2, 3}) = 4
...

G(2m - 1) = m
G(2m) = m - 1
"""

import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

nim_sum = reduce(lambda x, y: x ^ y, [(p + 1) // 2 if p % 2 else max(0, p // 2 - 1) for p in P])

print("koosaga" if nim_sum else "cubelover")