import sys
from functools import reduce

fibs = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309]

def mex(s):
    i = 0
    while i in s:
        i += 1

    return i

N = int(sys.stdin.readline().rstrip())
P = list(map(int, sys.stdin.readline().split()))

maximum = max(P)
G = [0] * (maximum + 1)

for i in range(1, maximum + 1):
    temp = set()
    for fib in fibs:
        if i - fib < 0:
            break
        
        temp.add(G[i - fib])

    G[i] = mex(temp)

result = reduce(lambda x, y: x ^ y, [G[p] for p in P])

print("koosaga" if result else "cubelover")