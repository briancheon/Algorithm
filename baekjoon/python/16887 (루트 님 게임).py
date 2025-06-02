"""
G(0) = G(1) = G(2) = G(3) = 0

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

G = [0] * 10001

for i in range(4, 10001):
    temp = set()
    for j in range(i):
        if i <= j ** 4 <= i ** 2:
            temp.add(G[j])
    G[i] = mex(temp)

결과
0 0 0 0 1 1 ... 2 2 ... 0 0 ... 3 3 ... 1 1 ... 2 2

구간
0: 0~3
1: 4~15
2: 16~81
0: 82~6723
3: 6724~50625
1: 50626~2562991875
2: 2562991876~
"""

import sys
from math import log2

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

nim_sum = 0
for Ai in A:
    if Ai <= 3 or 82 <= Ai <= 6723:
        temp_nim = 0

    elif 4 <= Ai <= 15 or 50626 <= Ai <= 2562991875:
        temp_nim = 1

    elif 16 <= Ai <= 81 or Ai > 2562991876:
        temp_nim = 2

    else:
        temp_nim = 3

    nim_sum ^= temp_nim

print("koosaga" if nim_sum else "cubelover")