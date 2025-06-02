import sys
import math

def fpow(n, p):
    if p == 0:
        return 1

    half = fpow(n, p // 2)
    if p % 2 == 0:
        return half * half
    else:
        return half * half * n

print(fpow(2, int(1e18)))