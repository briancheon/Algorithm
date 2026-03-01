import sys

def mex(s):
    i = 0
    while i in s:
        i += 1
    return i

M = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().split()))

G = [0] * 2501

for i in range(1, 2501):
    temp = set()
    for j in a:
        if i - j < 0:
            break
        temp.add(G[i - j])

    G[i] = mex(temp)

start_idx = 0
cycle = None
for i in range(22, 1500):
    for j in range(22, 1000):
        if G[i:i + j] == G[i + j:i + 2 * j]:
            cycle = G[i:i + j]
            start_idx = i
            break

cnt = len(list(filter(lambda x: x == 0, G[:start_idx])))

for i in range(len(cycle)):
    if cycle[i] == 0:
        cnt += (M - (start_idx + i)) // len(cycle) + 1

print(cnt - 1)