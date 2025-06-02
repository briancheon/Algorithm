import sys

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

n = int(sys.stdin.readline().rstrip())

G = [0] * (n + 1)
G[1] = G[2] = G[3] = 1
for i in range(4, n + 1):
    temp = set()
    for j in range((i + 1) // 2):
        temp.add(G[max(0, j - 2)] ^ G[i - j - 3])

    G[i] = mex(temp)

print(1 if G[n] else 2)