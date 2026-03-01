import sys

def mex(s):
    i = 0
    while i in s:
        i += 1

    return i

N = int(sys.stdin.readline().rstrip())

G = [0] * (N + 1)
G[2] = 1

for i in range(3, N + 1):
    temp = set()
    for j in range(i - 1):
        temp.add(G[j] ^ G[i - j - 2])

    G[i] = mex(temp)

print(1 if G[N] else 2)