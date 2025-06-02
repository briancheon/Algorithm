import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

if all(P[i] == 1 for i in range(N)):
    print("cubelover" if N % 2 else "koosaga")

else:
    result = reduce(lambda x, y: x ^ y, P)
    print("koosaga" if result else "cubelover")