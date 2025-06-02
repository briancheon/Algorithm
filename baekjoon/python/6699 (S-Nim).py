import sys
from functools import reduce

def mex(s):
    i = 0
    while i in s:
        i += 1
    
    return i

while True:
    k, *S = map(int, sys.stdin.readline().split())
    if k == 0:
        break

    G = [0] * 10001
    
    for i in range(1, 10001):
        temp = set()
        for s in S:
            if i - s >= 0:
                temp.add(G[i - s])

        G[i] = mex(temp)
    
    m = int(sys.stdin.readline().rstrip())
    positions = ""

    for _ in range(m):
        l, *h = map(int, sys.stdin.readline().split())
        h = [G[x] for x in h]

        result = reduce(lambda x, y: x ^ y, h)
        positions += "W" if result else "L"

    print(positions)