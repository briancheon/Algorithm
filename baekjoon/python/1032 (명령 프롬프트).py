import sys

N = int(sys.stdin.readline().rstrip())

names = []
for c in range(N):
    names.append(input())

base = list(names[0])
for a in range(1, N):
    for b in range(len(names[a])):
        if base[b] != names[a][b]:
            base[b] = "?"

print(*base, sep='')
