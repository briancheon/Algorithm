import sys

N = int(sys.stdin.readline().rstrip())

ls = {}

for c in range(N):
    num = int(int(sys.stdin.readline().rstrip()))
    if num not in ls.keys():
        ls[num] = 1
    else:
        ls[num] += 1

keys = sorted(list(ls.keys()))

for a in range(len(keys)):
    for b in range(ls[keys[a]]):
        print(keys[a])

