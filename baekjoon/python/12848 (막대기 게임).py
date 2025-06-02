import sys

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

n, m = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().rstrip() for _ in range(n)]

k = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().split()))

G = [0] * 1001
for i in range(1, 1001):
    temp = set()
    for j in p:
        if i - j < 0:
            break
        for k in range(i - j + 1):
            temp.add(G[k] ^ G[i - j - k])

    G[i] = mex(temp)

nim_sum = 0
for row in grid:
    for segment in row.split("@"):
        nim_sum ^= G[len(segment)]

print("nein" if nim_sum else "hyo123bin")