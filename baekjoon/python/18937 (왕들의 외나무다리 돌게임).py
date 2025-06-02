import sys
from functools import reduce

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
start = sys.stdin.readline().rstrip()

if start == "Whiteking":
    end = "Blackking"

else:
    end = "Whiteking"

nim_sum = reduce(lambda x, y: x ^ y, [Ai - 2 for Ai in A])
print(start if nim_sum else end)