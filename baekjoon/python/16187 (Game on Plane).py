import sys

def mex(s):
    i = 0
    while i in s:
        i += 1

    return i

G = [0] * (5001)
G[2] = 1

for i in range(3, 5001):
    temp = set()
    for j in range(i - 1):
        temp.add(G[j] ^ G[i - j - 2])

    G[i] = mex(temp)

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print("First" if G[N] else "Second")